import os
os.chdir('D:\Github\Introduction-to-Computer-Science-and-Programming-\Mid_Test')
from fixpoint import fixedPoint

# def sqrt(a):
#     def tryit(x):
#         return 0.5 * (a/x + x)
#     return fixedPoint(tryit, 0.0001)

def babylon(a):
    def test(x):
        return 0.5 * ((a / x) + x)
    return test

def sqrt(a):
    return fixedPoint(babylon(a), 0.0001)

sqrt(26)
