'''检查一个字符是否在一个以字符顺序排列的字符串之中。'''

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if char == aStr[len(aStr) // 2]:
        return True
    elif char != aStr and len(aStr) == 1:
        return False
    elif char < aStr[len(aStr) // 2]:
        return isIn(char, aStr[:len(aStr) // 2])
    elif char > aStr[len(aStr) // 2]:
        return isIn(char, aStr[len(aStr) // 2:])

isIn('a','akgw')
