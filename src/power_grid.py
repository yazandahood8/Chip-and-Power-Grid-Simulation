import numpy as np

class PowerGrid:
    def __init__(self, size):
        """
        Initialize a power grid with the given size.

        Args:
            size (int): The size of the grid (size x size).
        """
        self.size = size  # Size of the grid
        self.grid = np.zeros((size, size))  # Initialize the grid with zeros

    def apply_current(self, x, y, current):
        """
        Apply a current to a specific location in the grid.

        Args:
            x (int): The x-coordinate in the grid.
            y (int): The y-coordinate in the grid.
            current (float): The amount of current to apply.
        """
        if 0 <= x < self.size and 0 <= y < self.size:
            self.grid[x, y] += current  # Increment the current at the specified location

    def calculate_ir_drop(self):
        """
        Calculate the IR drop across the grid.

        Returns:
            tuple: The minimum and maximum current levels in the grid.
        """
        return np.min(self.grid), np.max(self.grid)  # Return min and max current levels as IR drop

    def simulate_em(self):
        """
        Simulate electromigration (EM) effects on the grid.

        Returns:
            tuple: Arrays of x and y coordinates where the current exceeds the mean.
        """
        # Placeholder for EM simulation
        affected_areas = np.where(self.grid > np.mean(self.grid))  # Find areas where current is above average
        return affected_areas  # Return the coordinates of affected areas
