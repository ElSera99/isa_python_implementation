# Import ISAs from class
from isas import ISA

# Instantiate class
my_architecture = ISA()

# Simple addition
my_architecture.CONST(5, 'Ra')  # First number to be added
my_architecture.CONST(7, 'Rb')  # Second number to be added
my_architecture.ADD('Ra', 'Rb', 'Rc')  # Result of addition
print(f"Result of addition: {my_architecture.registers['Ra']} + {my_architecture.registers['Rb']} = "
      f"{my_architecture.registers['Rc']}")
# Store to memory
my_architecture.ENCODE(my_architecture.registers['Rc'], 'SP')  # Encode as stream of bits and save to SP
my_architecture.STORE('SP', 0, 8)  # Store stream of bits from SP to memory
print(f"Encoded value of addition: {my_architecture.registers['SP']}")
# Load from memory
my_architecture.LOAD('Rd', 0, 8)  # Load stream of bits from memory and save to Rd
my_architecture.DECODE(my_architecture.registers['Rd'], 'Re')  # Decode stream of bits and save to Re
print(f"Retrieved data and decoded: {my_architecture.registers['Re']}")
my_architecture.HALT()  # End program
