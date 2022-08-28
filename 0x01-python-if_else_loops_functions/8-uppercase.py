#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) == 32:
            a = 32
        elif ord(i) in range(65, 91) or ord(i) in range(48, 58):
            a = ord(i)
        else:
            a = ord(i) - 32
        print("{}".format(chr(a)), end="")
    print("")
