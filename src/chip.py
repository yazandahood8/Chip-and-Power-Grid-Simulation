class Gate:
    def __init__(self, name, delay):
        # Initialize the gate with a name, delay, and empty input list.
        self.name = name  # Name of the gate (e.g., Buffer1, Inverter1)
        self.delay = delay  # Delay associated with this gate
        self.inputs = []  # List to store input gates
        self.output = None  # The output gate (if any)

    def set_output(self, gate):
        # Set the gate's output to the specified gate.
        self.output = gate  # Set the gate that this gate drives

    def add_input(self, gate):
        # Add a gate to the list of inputs for this gate.
        self.inputs.append(gate)  # Append the input gate to the list

    def get_delay(self):
        # Calculate and return the delay of this gate including its inputs.
        if not self.inputs:
            # If there are no inputs, return the gate's delay.
            return self.delay
        # If there are inputs, return the delay of this gate plus the maximum delay of its inputs.
        return self.delay + max(input_gate.get_delay() for input_gate in self.inputs)

class Chip:
    def __init__(self):
        # Initialize the chip with an empty list of gates.
        self.gates = []  # List to store all gates in the chip

    def add_gate(self, gate):
        # Add a gate to the chip's list of gates.
        self.gates.append(gate)  # Append the gate to the chip

    def calculate_delays(self):
        # Calculate the delays for all gates in the chip.
        return {gate.name: gate.get_delay() for gate in self.gates}
        # Create a dictionary where each gate's name is the key and its delay is the value

    def find_critical_path(self):
        # Find the critical path in the chip, which is the path with the maximum delay.
        max_delay = -1  # Initialize the maximum delay to a very low value
        critical_gate = None  # Initialize the critical gate variable
        for gate in self.gates:
            # Iterate through each gate in the chip
            delay = gate.get_delay()  # Get the delay for the current gate
            if delay > max_delay:
                # If the current gate's delay is greater than the maximum delay found so far
                max_delay = delay  # Update the maximum delay
                critical_gate = gate.name  # Update the critical gate name
        return critical_gate, max_delay
        # Return the name of the critical gate and the maximum delay
