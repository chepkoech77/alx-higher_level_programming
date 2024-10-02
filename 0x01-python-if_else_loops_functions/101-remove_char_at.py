#!/usr/bin/python3
def remove_char_at(input_str, n):
    if 0 <= n < len(input_str):
        res = input_str[:n] + input_str[n + 1:]
        return res
    else:
        return input_str
