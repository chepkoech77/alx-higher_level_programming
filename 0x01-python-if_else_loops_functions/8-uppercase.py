#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if char >= 'a' and char <= 'z':
            upper = ord(char) - ord('a') + ord('A')
            result += chr(upper)
        else:
            result += char

    print("{}\n".format(result), end="")
