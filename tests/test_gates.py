# tests/test_gates.py
import sys
import os
import unittest

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from gates import Gate

class TestGate(unittest.TestCase):
    def test_gate_delay(self):
        buffer1 = Gate("Buffer1", 1)
        buffer2 = Gate("Buffer2", 1)
        inverter1 = Gate("Inverter1", 2)

        buffer1.set_output(buffer2)
        buffer2.set_output(inverter1)

        inverter1.add_input(buffer2)
        buffer2.add_input(buffer1)

        self.assertEqual(inverter1.get_delay(), 4)

if __name__ == '__main__':
    unittest.main()
