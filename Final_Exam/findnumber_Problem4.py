# # 6.00.1x Final Exam
# def secretNum(guess):
#     secret = 10
#     if guess > secret:
#         return 1
#     elif guess < secret:
#         return -1
#     elif guess == secret:
#         return 0
#
# def findNum():
#     guess = 1
#     if secretNum(guess) == 0:
#         return guess
#     foundFlag = True
#     while foundFlag:
#         sign = secretNum(guess)
#         if sign == -1:
#             guess *= 2
#         elif sign == 1:
#             guess -= 1
#         elif sign == 0:
#             return guess
#
# print findNum()
def isMyNumber(guess):
    secret = -24 # 10 原来只要大于的都没问题。因第一个条件判断 == 1 错了，应为 == 0.
    if guess > secret:
        return 1
    elif guess < secret:
        return -1
    elif guess == secret:
        return 0

def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number.
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number

    returns: integer, the secret number
    '''
    guess = 1
    if isMyNumber(guess) == 0:
        return guess
    foundNumber = False
    while not foundNumber:
        sign = isMyNumber(guess)
        if sign == -1:
            guess *= 2
        elif sign == 0:
            foundNumber = True
        else:
            guess -= 1
    return guess

print jumpAndBackpedal(isMyNumber)
