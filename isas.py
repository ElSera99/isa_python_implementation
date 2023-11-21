class ISA:
    """ This class represents the set of instructions that the CPU can execute """
    def __init__(self):
        # Registers of CPU: 8
        # Two extra registers for IP and SP
        self.registers = {"Ra": 0,
                          "Rb": 0,
                          "Rc": 0,
                          "Rd": 0,
                          "Re": 0,
                          "Rf": 0,
                          "Rg": 0,
                          "Rh": 0,
                          "IP": 0,  # Instruction pointer indicates the number of instruction that is being executed
                          "SP": 0  # Stack pointer indicates the stack pointer where the data is going to be stored
                          }
        # Simulation of the memory in a computer
        self.memory = [0] * 1024

    def ADD(self, reg1, reg2, reg3):
        """ Add to numbers stated in register 1 and register 2 and store in register 3 """
        self.registers[reg3] = self.registers[reg1] + self.registers[reg2]
        self.registers['IP'] += 1
        return self.registers[reg3]

    def SUB(self, reg1, reg2, reg3):
        self.registers[reg3] = self.registers[reg1] - self.registers[reg2]
        self.registers['IP'] += 1
        return self.registers[reg3]

    def MUL(self, reg1, reg2, reg3):
        self.registers[reg3] = self.registers[reg1] * self.registers[reg2]
        self.registers['IP'] += 1
        return self.registers[reg3]

    def DIV(self, reg1, reg2, reg3):
        self.registers[reg3] = self.registers[reg1] / self.registers[reg2]
        self.registers['IP'] += 1
        return self.registers[reg3]

    def INC(self, reg1):
        """ Increase in one the number in the register and save into the same register """
        self.registers[reg1] = self.registers[reg1] + 1
        self.registers['IP'] += 1
        return self.registers[reg1]

    def DEC(self, reg1):
        """ Decrease in one the number in the register and save into the same register """
        self.registers[reg1] = self.registers[reg1] - 1
        self.registers['IP'] += 1
        return self.registers[reg1]

    def CMP(self, op, reg1, reg2, reg3):
        """ Comparison of two numbers and store result into register 3 """
        operators = {1: self.registers[reg1] < self.registers[reg2],
                     2: self.registers[reg1] > self.registers[reg2],
                     3: self.registers[reg1] <= self.registers[reg2],
                     4: self.registers[reg1] >= self.registers[reg2],
                     5: self.registers[reg1] == self.registers[reg2],
                     6: self.registers[reg1] != self.registers[reg2]
                     }
        self.registers['IP'] += 1
        self.registers[reg3] = operators[op]
        return self.registers[reg3]

    def CONST(self, value, reg1):
        """ Define a constant that can be operated with the previously defined methods """
        self.registers[reg1] = value
        self.registers['IP'] += 1
        return self.registers[reg1]

    # reg_store = CPU register to store, reg_data = RAM register to load from
    def LOAD(self, reg_store, reg_data, offset):
        """ Load data from a sector of the memory, will load bit stream from the sectors of the memory """
        self.registers[reg_store] = self.memory[reg_data]
        self.registers['IP'] += 1
        return self.registers[reg_store]

    # reg_store = CPU register where data is temporarily stored, reg_data = RAM register to save data to
    def STORE(self, reg_store, reg_data, offset):
        """ Will store a stream of bits into the memory """
        self.memory[reg_data] = self.registers[reg_store]
        self.registers['IP'] += 1
        return self.memory[reg_data]

    def JMP(self, reg_data, offset):
        """ Will jump from one sector of the memory to another """
        self.registers['SP'] = self.DECODE(self.memory[reg_data], 'SP')
        self.registers['IP'] += 1
        return self.registers['SP']

    def HALT(self):
        """ Will stop execution of program """
        print(f"IP:{self.registers['IP']} - End of Program")
        exit()

    def ENCODE(self, value, reg1):
        """ Take an integer and transform into a stream of bits """
        result = []
        while value // 2 != 0:
            result.append(value % 2)
            value //= 2
            if value == 1:
                result.append(1)
        result = result[::-1]

        self.registers[reg1] = result
        self.registers['IP'] += 1

        return result

    def DECODE(self, value, reg1):
        """ Take a stream of bits and transform into an integer """
        result = 0
        power = len(value) - 1
        for element in value:
            result += element * (2 ** power)
            power -= 1

        self.registers[reg1] = result
        self.registers['IP'] += 1

        return result


if __name__ == '__main__':
    # My architecture instance
    my_architecture = ISA()
