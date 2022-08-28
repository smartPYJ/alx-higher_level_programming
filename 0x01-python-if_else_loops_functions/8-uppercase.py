#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(32, 91):
            a = ord(i)
        else:
            a = ord(i) - 32
        print("{}".format(chr(a)), end="")
    print("")
