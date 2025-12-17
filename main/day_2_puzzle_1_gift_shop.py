"""
--- Day 2: Gift Shop ---

You get inside and take the elevator to its only other stop: the gift shop. "Thank you for visiting the North Pole!" gleefully exclaims a nearby sign. You aren't sure who is even allowed to visit the North Pole, but you know you can access the lobby through here, and from there you can access the rest of the North Pole base.

As you make your way through the surprisingly extensive selection, one of the clerks recognizes you and asks for your help.

As it turns out, one of the younger Elves was playing on a gift shop computer and managed to add a whole bunch of invalid product IDs to their gift shop database! Surely, it would be no trouble for you to identify the invalid product IDs for them, right?

They've even checked most of the product ID ranges already; they only have a few product ID ranges (your puzzle input) that you'll need to check. For example:

11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
(The ID ranges are wrapped here for legibility; in your input, they appear on a single long line.)

The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).

Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)

Your job is to find all of the invalid IDs that appear in the given ranges. In the above example:

11-22 has two invalid IDs, 11 and 22.
95-115 has one invalid ID, 99.
998-1012 has one invalid ID, 1010.
1188511880-1188511890 has one invalid ID, 1188511885.
222220-222224 has one invalid ID, 222222.
1698522-1698528 contains no invalid IDs.
446443-446449 has one invalid ID, 446446.
38593856-38593862 has one invalid ID, 38593859.
The rest of the ranges contain no invalid IDs.
Adding up all the invalid IDs in this example produces 1227775554.

What do you get if you add up all of the invalid IDs?


"""


def is_invalid_id(num: int) -> bool:
    """Check if a number is an invalid ID (digit sequence repeated twice)."""
    s = str(num)
    length = len(s)

    # Must have even length to be repeated twice
    if length % 2 != 0:
        return False

    # Split in half and check if both halves are equal
    mid = length // 2
    first_half = s[:mid]
    second_half = s[mid:]

    # Check for leading zeros (first half shouldn't start with 0)
    if first_half[0] == '0':
        return False

    return first_half == second_half


def parse_ranges(input_str: str) -> list[tuple[int, int]]:
    """Parse the input string into a list of ranges."""
    ranges = []
    for range_str in input_str.strip().split(','):
        if '-' in range_str:
            start, end = range_str.split('-')
            ranges.append((int(start), int(end)))
    return ranges


def find_invalid_ids_in_range(start: int, end: int) -> list[int]:
    """Find all invalid IDs in a given range."""
    invalid_ids = []
    for num in range(start, end + 1):
        if is_invalid_id(num):
            invalid_ids.append(num)
    return invalid_ids


def solve() -> int:
    """Solve the puzzle and return the sum of all invalid IDs."""
    with open('day_2_puzzle_1_gift_shop_input.txt', 'r') as f:
        input_data = f.read()

    ranges = parse_ranges(input_data)
    total_sum = 0

    for start, end in ranges:
        invalid_ids = find_invalid_ids_in_range(start, end)
        total_sum += sum(invalid_ids)

    return total_sum


if __name__ == '__main__':
    result = solve()
    print(f"Sum of all invalid IDs: {result}")
