#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

program_filename = sys.argv[1]

cpu = CPU()

cpu.load(program_filename)

cpu.run()

