inst_len = ((ir & 0b11000000) >> 6) + 1   # 3
pc += inst_len
