#! /usr/bin/env python

from snap.snap import snap

def test():

    assert "1" == snap(1)
    assert "Crackle" == snap(3)
    assert "Pop" == snap(5)
    assert "CracklePop" == snap(15)

    def tricky(n):
        assert "CracklePop" == snap(n)

    ## steps of 15 mean the number will be divisible by 3 and 5
    [ tricky(n) for n in range(0, 100 + 1, 15) ]

if __name__ == "__main__":
    test()
