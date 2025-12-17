"""--- Part Two ---

The clerk quickly discovers that there are still invalid IDs in the ranges in your list. Maybe the young Elf was doing other silly patterns as well?

Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.

From the same example as before:

11-22 still has two invalid IDs, 11 and 22.
95-115 now has two invalid IDs, 99 and 111.
998-1012 now has two invalid IDs, 999 and 1010.
1188511880-1188511890 still has one invalid ID, 1188511885.
222220-222224 still has one invalid ID, 222222.
1698522-1698528 still contains no invalid IDs.
446443-446449 still has one invalid ID, 446446.
38593856-38593862 still has one invalid ID, 38593859.
565653-565659 now has one invalid ID, 565656.
824824821-824824827 now has one invalid ID, 824824824.
2121212118-2121212124 now has one invalid ID, 2121212121.
Adding up all the invalid IDs in this example produces 4174379265.

What do you get if you add up all of the invalid IDs using these new rules?

"""


def is_invalid_id(num: int) -> bool:
    """Check if a number is an invalid ID (digit sequence repeated at least twice)."""
    s = str(num)
    length = len(s)

    # Check all possible pattern lengths from 1 to length//2
    for pattern_len in range(1, length // 2 + 1):
        # Check if the total length is divisible by pattern length
        if length % pattern_len == 0:
            pattern = s[:pattern_len]

            # Check for leading zeros
            if pattern[0] == '0':
                continue

            # Check if the entire string is this pattern repeated
            is_repeated = True
            num_repeats = length // pattern_len

            # Must be repeated at least twice
            if num_repeats >= 2:
                for i in range(num_repeats):
                    start = i * pattern_len
                    end = start + pattern_len
                    if s[start:end] != pattern:
                        is_repeated = False
                        break

                if is_repeated:
                    return True

    return False


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
