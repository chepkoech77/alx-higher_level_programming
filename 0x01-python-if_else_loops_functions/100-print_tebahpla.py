#!/usr/bin/python3
def print_rev():
    for char_code in range(ord('z'), ord('A') -1, -1):
        case_adjusted_char_code = char_code + 32 if char_code % 2 == 0 else char_code
        print("{}".format(chr(case_adjusted_char_code)), end="")

print_rev()
