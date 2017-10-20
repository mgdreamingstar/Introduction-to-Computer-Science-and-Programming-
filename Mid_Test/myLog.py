def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    result = 0
    multi = 1
    while multi * b <= x:
        result += 1
        multi *= b
    return result


print myLog(27, 3)
print myLog(26, 3)
print myLog(28, 3)
print myLog(4, 16)
print myLog(5, 17)
print myLog(54, 6)
print myLog(69, 5)
print myLog(109, 4)
