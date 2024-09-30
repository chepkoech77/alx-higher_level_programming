#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    arg_len = len(argv)
    if arg_len == 1:
        print("{} arguments.".format(0))
    elif arg_len == 2:
        print("{} argument:".format(arg_len - 1))
    else:
        print("{} arguments:".format(arg_len - 1))
    if arg_len >= 2:
        for i in range(1, arg_len):
            print("{}: {}".format(i, argv[i]))
