"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__ (self, start=0):
        self.start = self.next = start

    def __repr__(self):
        return f"Next serial number = {next_serial_number}"

    def generate(self):
        self.next += 1
        next_serial_number = self.next - 1
        return next_serial_number
        

    def reset(self):
        self.next = self.start
