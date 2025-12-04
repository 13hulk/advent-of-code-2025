"""
--- Part Two ---

You're sure that's the right password, but the door won't open. You knock, but nobody answers. You build a snowman while you think.

As you're rolling the snowballs for your snowman, you find another security document that must have fallen into the snow:

"Due to newer security protocols, please use password method 0x434C49434B until further notice."

You remember from the training seminar that "method 0x434C49434B" means you're actually supposed to count the number of times any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one.

Following the same rotations as in the above example, the dial points at zero a few extra times during its rotations:

The dial starts by pointing at 50.
The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
The dial is rotated L30 to point at 52.
The dial is rotated R48 to point at 0.
The dial is rotated L5 to point at 95.
The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
The dial is rotated L55 to point at 0.
The dial is rotated L1 to point at 99.
The dial is rotated L99 to point at 0.
The dial is rotated R14 to point at 14.
The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.
In this example, the dial points at 0 three times at the end of a rotation, plus three more times during a rotation. So, in this example, the new password would be 6.

Be careful: if the dial were pointing at 50, a single rotation like R1000 would cause the dial to point at 0 ten times before returning back to 50!

Using password method 0x434C49434B, what is the password to open the door?
"""


class SafeLockAdvanced:
    def __init__(self):
        self.position = 50  # Dial starts at 50
        self.zero_count = 0  # Count of times dial points at 0

    def count_zeros_in_rotation(self, direction: str, distance: int) -> int:
        """
        Count how many times the dial points at 0 during a rotation.

        The dial has positions 0-99. When rotating, we count every time
        we pass through position 0.

        Args:
            direction: 'L' for left or 'R' for right
            distance: Number of clicks to rotate

        Returns:
            Number of times the dial points at 0 during this rotation
        """
        p = self.position
        a = distance

        if direction == "R":
            # Right rotation: we visit positions p+1, p+2, ..., p+a (mod 100)
            # We hit 0 when p+i is a multiple of 100
            # Count = floor((p+a)/100) - floor(p/100)
            count = (p + a) // 100 - p // 100
        else:  # direction == 'L'
            # Left rotation: we visit positions p-1, p-2, ..., p-a (mod 100)
            # We hit 0 when p-i is a multiple of 100
            # Count = floor((p-1)/100) - floor((p-a-1)/100)
            count = (p - 1) // 100 - (p - a - 1) // 100

        return count

    def rotate(self, direction: str, distance: int):
        """
        Rotate the dial in the given direction by the specified distance.
        Counts all times the dial points at 0 during the rotation.

        Args:
            direction: 'L' for left (toward lower numbers) or 'R' for right (toward higher numbers)
            distance: Number of clicks to rotate
        """
        # Count zeros during the rotation
        zeros_during = self.count_zeros_in_rotation(direction, distance)
        self.zero_count += zeros_during

        # Update position
        if direction == "L":
            self.position = (self.position - distance) % 100
        elif direction == "R":
            self.position = (self.position + distance) % 100
        else:
            raise ValueError(f"Invalid direction: {direction}")

    def process_rotations(self, rotations: list[str]) -> int:
        """
        Process a list of rotation instructions and return the password.

        Args:
            rotations: List of rotation instructions (e.g., ['L68', 'R48'])

        Returns:
            The number of times the dial points at 0 (the password)
        """
        for rotation in rotations:
            direction = rotation[0]
            distance = int(rotation[1:])
            self.rotate(direction, distance)

        return self.zero_count

    def get_password(self) -> int:
        """Return the password (number of times dial pointed at 0)."""
        return self.zero_count


def solve_puzzle(input_data: str) -> int:
    """
    Solve the puzzle with the given input data.

    Args:
        input_data: String containing rotation instructions, one per line

    Returns:
        The password to open the door
    """
    safe = SafeLockAdvanced()
    rotations = [line.strip() for line in input_data.strip().split("\n") if line.strip()]
    return safe.process_rotations(rotations)


# Example test case from the puzzle
def test_example():
    example_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

    result = solve_puzzle(example_input)
    print(f"Example result: {result}")
    assert result == 6, f"Expected 6, got {result}"
    print("✓ Example test passed!")


def test_large_rotation():
    """Test the R1000 example from the puzzle description."""
    safe = SafeLockAdvanced()
    safe.position = 50

    # R1000 from position 50 should hit 0 ten times
    zeros = safe.count_zeros_in_rotation("R", 1000)
    print(f"R1000 from position 50 hits 0: {zeros} times")
    assert zeros == 10, f"Expected 10, got {zeros}"
    print("✓ Large rotation test passed!")


if __name__ == "__main__":
    # # Run the example test
    # test_example()

    # # Run the large rotation test
    # test_large_rotation()

    # Try to solve with actual input if available
    try:
        with open("day_1_puzzle_2_input.txt", "r") as f:
            puzzle_input = f.read()

        password = solve_puzzle(puzzle_input)
        print(f"\nThe password is: {password}")
    except FileNotFoundError:
        print(
            "\nNo input file found. Place your puzzle input in 'day_1_puzzle_2_input.txt'"
        )
