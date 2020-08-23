from __future__ import print_function
def binary(n):
    if n>1:
        binary(n//2)
    print (n%2, end="")
binary(33)
print()