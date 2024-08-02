import argparse
import matplotlib.pyplot as plt  # Importing the library for visualizing data
from .chip import Chip  # Importing the Chip class from the local module
from .gates import Gate  # Importing the Gate class from the local module
from .power_grid import PowerGrid  # Importing the PowerGrid class from the local module

def create_chip():
    # Create and configure gates for the chip
    buffer1 = Gate("Buffer1", 1)  # Create a buffer gate with delay 1
    buffer2 = Gate("Buffer2", 1)  # Create another buffer gate with delay 1
    inverter1 = Gate("Inverter1", 2)  # Create an inverter gate with delay 2

    # Define connections between gates
    buffer1.set_output(buffer2)  # Buffer1 drives Buffer2
    buffer2.set_output(inverter1)  # Buffer2 drives Inverter1
    inverter1.add_input(buffer2)  # Inverter1 receives input from Buffer2
    buffer2.add_input(buffer1)  # Buffer2 receives input from Buffer1

    # Create a chip and add the gates
    chip = Chip()  # Instantiate a Chip object
    chip.add_gate(buffer1)  # Add Buffer1 to the chip
    chip.add_gate(buffer2)  # Add Buffer2 to the chip
    chip.add_gate(inverter1)  # Add Inverter1 to the chip

    return chip  # Return the configured chip

def create_power_grid():
    # Create and configure a power grid
    power_grid = PowerGrid(10)  # Instantiate a PowerGrid object with a 10x10 grid
    power_grid.apply_current(5, 5, 0.2)  # Apply a current to a point in the grid
    return power_grid  # Return the configured power grid

def visualize_power_grid(power_grid):
    # Visualize the power grid using a heatmap
    plt.imshow(power_grid.grid, cmap='hot', interpolation='nearest')  # Display the power grid as a heatmap
    plt.title('Power Grid Visualization')  # Set the title of the plot
    plt.colorbar()  # Show the color scale
    plt.show()  # Display the plot

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Chip Design Simulation")  # Create an ArgumentParser object
    parser.add_argument('--chip', action='store_true', help="Simulate chip delays and critical path")  # Option to simulate chip
    parser.add_argument('--power', action='store_true', help="Simulate power grid IR drop and EM")  # Option to simulate power grid

    args = parser.parse_args()  # Parse the arguments

    if args.chip:
        # If the --chip argument is provided, simulate chip delays and critical path
        chip = create_chip()  # Create a chip
        delays = chip.calculate_delays()  # Calculate delays for all gates
        print("Gate Delays:", delays)  # Print delays
        critical_gate, critical_delay = chip.find_critical_path()  # Find the critical path
        print(f"Critical Path: {critical_gate} with delay {critical_delay}")  # Print the critical path and its delay

    if args.power:
        # If the --power argument is provided, simulate power grid IR drop and EM
        power_grid = create_power_grid()  # Create a power grid
        ir_drop = power_grid.calculate_ir_drop()  # Calculate IR drop
        print(f"IR Drop: {ir_drop}")  # Print IR drop
        em_affected_areas = power_grid.simulate_em()  # Simulate EM effects
        print(f"EM Affected Areas: {list(zip(*em_affected_areas))}")  # Print affected areas
        visualize_power_grid(power_grid)  # Visualize the power grid

if __name__ == '__main__':
    main()  # Run the main function if the script is executed directly
