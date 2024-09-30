#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    arg_len = len(argv)

    if arg_len > 1:
        for i in range(1, arg_len):
            sum += int(argv[i])
    print("{}".format(sum))
