'''计算字符串长度'''

def lenIter(aStr):
    '''
    aStr: a string
    return: int, the length of aStr
    '''
    if aStr == '':
        return 0 # 终止递归
    else:
        return lenIter(aStr[1:]) + 1


lenIter('abc')
