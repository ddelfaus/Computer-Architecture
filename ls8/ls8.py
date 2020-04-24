#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

program_filename = sys.argv[1]

# "ls8\examples\stack.ls8"
# "ls8\examples\call.ls8"
# sys.argv[1]
cpu = CPU()

cpu.load(program_filename)

cpu.run()

