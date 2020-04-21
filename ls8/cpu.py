"""CPU functionality."""

import sys
# commands
LDI = 0b10000010
HLT = 0b00000001
PRN = 0b01000111
MUL = 0b10100010

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.IR = 0
        self.pc = 0  # counter
        self.running = True
        self.branchtable = {}
        self.branchtable[LDI] = self.handle_LDI
        self.branchtable[PRN] = self.handle_PRN
        self.branchtable[MUL] = self.handle_MUL
        self.branchtable[HLT] = self.handle_HLT

    def handle_LDI(self):
        
        operand_a = self.ram_read(self.pc + 1)         
        operand_b = self.ram_read(self.pc + 2)      
        self.reg[operand_a] = operand_b

    def handle_HLT(self):
        self.running = False


    def handle_PRN(self):
        operand_a = self.ram_read(self.pc + 1)
        operand_b = self.reg[operand_a]
        print(operand_b)


    def handle_MUL(self):
        operand_a = self.ram_read(self.pc + 1)
        operand_b = self.ram_read(self.pc + 2)
        self.reg[operand_a]= self.reg[operand_a] * self.reg[operand_b]
    def load(self, filename):
        """Load a program into memory."""

        address = 0


        #loading from example files



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

        with open(filename) as f:
            for line in f:
                line = line.split('#')
                line = line[0].strip()

                if line == '':
                    continue
                
                self.ram[address] = int(line,2)
                
                # print(line)     
                address +=1
                
       



        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1
        

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
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
            self.IR = self.ram[self.pc]

            if self.IR in self.branchtable:
                self.branchtable[self.IR]()
                print(((self.IR & 0b11000000) >> 6) +1 )
                pc_len = ((self.IR & 0b11000000) >> 6) + 1
           
                self.pc += pc_len



            else:
                print("unknown instruction")
                running = False
       
       
       
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
