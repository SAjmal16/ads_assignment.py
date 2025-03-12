import unittest

def check_level(level):
    """
    Recursively checks if a game level is feasible.

    Parameters:
    level (list): A list of non-negative integers representing the game level.

    Returns:
    bool: True if the player can reach the last index, False otherwise.
    """
    def helper(position, visited):
        """ Helper function to handle recursion with tracking of visited indices. """
        # Base cases
        if position >= len(level) - 1:
            return True  # Reached the last index
        if level[position] == 0:
            return False  # Landed on a mine
        if position in visited:
            return False  # Prevent infinite loops

        visited.add(position)  # Mark current position as visited

        # Try all possible jumps from 1 to the max jump length at the current position
        for jump in range(1, level[position] + 1):
            next_position = position + jump
            if next_position < len(level) and helper(next_position, visited):
                return True  # Found a valid path

        return False  # No valid path found

    return helper(0, set())  # Start from position 0 with an empty set of visited positions


# Unit Tests to Verify Correctness
class TestCheckLevel(unittest.TestCase):
    """Unit tests for the check_level function."""

    def test_feasible_levels(self):
        self.assertTrue(check_level([3, 1, 2, 0, 4, 0, 1]))  # Example from Figure 1
        self.assertTrue(check_level([2, 3, 1, 1, 4]))  # Classic jump game problem
        self.assertTrue(check_level([1, 2, 3, 4, 5]))  # Increasing steps

    def test_unfeasible_levels(self):
        self.assertFalse(check_level([3, 2, 1, 0, 2, 0, 2]))  # Example from Figure 2
        self.assertFalse(check_level([1, 0, 2, 3]))  # Blocked immediately
        self.assertTrue(check_level([0]))  # Single mine
        self.assertFalse(check_level([1, 1, 0, 1]))  # Trapped before reaching the end

    def test_edge_cases(self):
        self.assertTrue(check_level([1]))  # Single-element list, already at the end
        self.assertTrue(check_level([2, 0]))  # Can jump directly to the last index
        self.assertFalse(check_level([0, 2]))  # First element is a mine

if __name__ == "__main__":
    unittest.main()
