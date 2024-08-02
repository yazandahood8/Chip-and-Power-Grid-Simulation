# Chip and Power Grid Simulation

## Overview

This project simulates the design and analysis of a chip and its power grid. It calculates gate delays, critical paths, IR drops, and EM affected areas. The project includes a command-line interface for simulation and visualization.

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yazandahood8/Chip-and-Power-Grid-Simulation.git
    cd Chip-and-Power-Grid-Simulation
    ```

2. **Install dependencies:**

    Create a `requirements.txt` file in the root directory with the following content if you don't have it yet:

    ```
    numpy
    matplotlib
    ```

    Then install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run simulations:**

    - For chip simulation:
    
        ```bash
        python main.py --chip
        ```

    - For power grid simulation:
    
        ```bash
        python main.py --power
        ```

## Files

- `src/chip.py`: Defines the `Chip` class for chip simulation.
- `src/gates.py`: Defines the `Gate` class for gates used in the chip.
- `src/power_grid.py`: Defines the `PowerGrid` class for power grid simulation.
- `src/cli.py`: Command-line interface for running simulations.
- `tests/test_chip.py`: Unit tests for the `Chip` class.
- `tests/test_power_grid.py`: Unit tests for the `PowerGrid` class.

## Contributing

Feel free to open issues or submit pull requests. Contributions are welcome!


