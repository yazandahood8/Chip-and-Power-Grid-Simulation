class Gate:
    def __init__(self, name, delay):
        self.name = name  # Name of the gate
        self.delay = delay  # Delay of the gate
        self.inputs = []  # List of input gates
        self.output = None  # Output gate

    def add_input(self, gate):
        """
        Add an input gate to this gate's list of inputs.

        Args:
            gate (Gate): The input gate to be added.
        """
        self.inputs.append(gate)  # Append the input gate to the inputs list

    def set_output(self, gate):
        """
        Set the output gate for this gate.

        Args:
            gate (Gate): The output gate to be set.
        """
        self.output = gate  # Assign the provided gate as the output

    def get_delay(self):
        """
        Get the delay of this gate. This method returns the delay
        of this gate itself. It does not include delays from the input gates.

        Returns:
            int: The delay of the gate.
        """
        return self.delay  # Return the delay of this gate
