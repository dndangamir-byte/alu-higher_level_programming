#!/usr/bin/python3
def uppercase(str):
    print("{}".format("".join(chr(ord(c) - 32) if 97 <= ord(c) <= 122 else chr(ord(c)) for c in str)))
