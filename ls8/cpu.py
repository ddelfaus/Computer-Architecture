"""CPU functionality."""

import sys
# commands
LDI = 0b10000010
HLT = 0b00000001
PRN = 0b01000111
MUL = 0b10100010
PUSH = 0b01000101
POP = 0b01000110
CALL = 0b01010000
ADD = 0b10100000
RET = 0b00010001



class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.SP = 7
        self.reg[self.SP] = 0xF4
        self.IR = 0
        self.pc = 0  # counter
        self.running = True
        self.branchtable = {}
        self.branchtable[LDI] = self.handle_LDI
        self.branchtable[PRN] = self.handle_PRN
        self.branchtable[MUL] = self.handle_MUL
        self.branchtable[ADD] = self.handle_ADD
        self.branchtable[HLT] = self.handle_HLT
        self.branchtable[PUSH] = self.handle_PUSH
        self.branchtable[POP] = self.handle_POP
        self.branchtable[CALL] = self.handle_CALL
        self.branchtable[RET] = self.handle_RET

    def handle_LDI(self, a, b):

        # operand_a = self.ram_read(self.pc + 1)
        # operand_b = self.ram_read(self.pc + 2)
        self.reg[a] = b
        self.pc += 3

    def handle_HLT(self):
        self.running = False
        # self.pc +=1

    def handle_PRN(self, a):
        # operand_a = self.ram_read(self.pc + 1)
        # operand_b = self.reg[operand_a]

        print(self.reg[a], "print")
        self.pc += 2

    def handle_ADD(self, a, b):
        self.reg[a] = self.reg[a] + self.reg[b]

        self.pc += 3

    def handle_MUL(self, a, b):
        # operand_a = self.ram_read(self.pc + 1)
        # operand_b = self.ram_read(self.pc + 2)
        # self.reg[operand_a]= self.reg[operand_a] * self.reg[operand_b]
        self.reg[a] = self.reg[a] * self.reg[b]

        self.pc += 3

    def handle_PUSH(self, a):

        # operand_a = self.ram_read(self.pc + 1)
        # operand_b = self.reg[operand_a]

        self.reg[self.SP] -= 1
        self.ram[self.reg[self.SP]] = self.reg[a]
        self.pc += 2

    def handle_POP(self, a):
        # operand_a = self.ram_read(self.pc + 1)
        # operand_b = self.ram_read(self.reg[self.SP])
        self.reg[a] = self.ram[self.reg[self.SP]]
        self.reg[self.SP] += 1
        # self.reg[operand_a] = operand_b
        self.pc += 2

    def handle_CALL(self, a):
        # breakpoint()
        return_address = self.pc +2
    
        self.pc -= 1
        self.ram[self.reg[self.SP]] = return_address
        self.pc = self.reg[a]
     
         # print(operand_a, "test")
        # to_stack = self.pc + 2

        # self.IR = operand_a
        # print(self.IR)
        # return dest_addr

    def handle_RET(self):
      
        self.pc = self.ram[self.reg[self.SP]]
        self.reg[self.SP] += 1

       

    def load(self, filename):
        """Load a program into memory."""

        address = 0
        # loading from example files


        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010,  # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111,  # PRN R0
        #     0b00000000,
        #     0b00000001,  # HLT
        # ]
        count = 0
        with open(filename) as f:
            for line in f:
                line = line.split('#')
                line = line[0].strip()

                if line == '':
                    continue

                self.ram[address] = int(line, 2)

                count = count + 1
                print(line)
                # print(count)
                address += 1


        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc

        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

    def ram_read(self, mar):

        return self.ram[mar]

    def ram_write(self, mar, mdr):
        self.ram[mar] = mdr

    def run(self):
        """Run the CPU."""

        while self.running is True:
            self.IR = self.ram_read(self.pc)

            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)

            operands = self.IR >> 6

            if self.IR in self.branchtable:
               
                if operands == 0:
                    self.branchtable[self.IR]()

                elif operands == 1:

                    self.branchtable[self.IR](operand_a)

                elif operands == 2:

                    self.branchtable[self.IR](operand_a, operand_b)

            else:
                print("unknown instruction")

                break


        # while self.running is True:
        #     IR = self.ram[self.pc]
        #     # print(self.IR)

        #     if self.IR in self.branchtable:
        #         self.branchtable[self.IR]()

        #         pc_len = ((self.IR & 0b11000000) >> 6) + 1

        #         self.pc += pc_len

        #     else:
        #         print("unknown instruction")
        #         running = False
        #         break

        # while self.running is True:
        #     self.IR = self.ram_read(self.pc)
        #     print(self.IR)

        #     if self.IR in self.branchtable:
        #         pc_value = self.branchtable[self.IR]()
        #         if pc_value == None:
        #             pc_len = ((self.IR & 0b11000000) >> 6) + 1

        #             self.pc += pc_len

        #         else:
        #             self.pc = pc_value

        #     else:

        #         print("unknown instruction")
        #         running = False
        #         break

        # IR = 0

        # running = True
        # while running is True:
        #     # get the starting memory
        #     IR = self.ram[self.pc]

        #     if IR == HLT:

        #         running = False

        #     elif IR == LDI:

        #         operand_a = self.ram_read(self.pc + 1)

        #         operand_b = self.ram_read(self.pc + 2)

        #         self.reg[operand_a] = operand_b
        #         self.pc += 3

        #     elif IR == PRN:

        #         operand_a = self.ram_read(self.pc + 1)
        #         operand_b = self.reg[operand_a]
        #         print(operand_b)
        #         self.pc += 2

        #     elif IR == MUL:
        #         operand_a = self.ram_read(self.pc + 1)
        #         operand_b = self.ram_read(self.pc + 2)
        #         self.reg[operand_a]= self.reg[operand_a] * self.reg[operand_b]
        #         self.pc += 3

        #     else:
        #         print("unknown instruction")
        #         running = False

        #     self.pc += 1
