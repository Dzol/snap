#! /usr/bin/env python

'''A program that prints out the numbers 1 to 100 (inclusive). If the
number is divisible by 3, print `Crackle' instead of the number. If
it's divisible by 5, print `Pop'. If it's divisible by both 3 and 5,
print `CracklePop'.

'''

def test():

    assert "1" == snap(1)
    assert "Crackle" == snap(3)
    assert "Pop" == snap(5)
    assert "CracklePop" == snap(15)

    def tricky(n):
        assert "CracklePop" == snap(n)

    ## steps of 15 mean the number will be divisible by 3 and 5
    [ tricky(n) for n in xrange(0, 100 + 1, 15) ]

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
                                                                                
