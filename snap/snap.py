#! /usr/bin/env python

'''A program that prints out the numbers 1 to 100 (inclusive). If the
number is divisible by 3, print `Crackle' instead of the number. If
it's divisible by 5, print `Pop'. If it's divisible by both 3 and 5,
print `CracklePop'.

'''

def snap(n):

    '''snap(n :: integer) :: string'''

    if n % 3 == 0 and n % 5 == 0:
        return "CracklePop"
    elif n % 3 == 0:
        return "Crackle"
    elif n % 5 == 0:
        return "Pop"
    else:
        return str(n)

if __name__ == "__main__":
    for i in xrange(1, 100 + 1):
        print snap(i)
