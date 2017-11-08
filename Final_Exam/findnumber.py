# 6.00.1x Final Exam
def secretNum(guess):
    secret = 10
    if guess > secret:
        return 1
    elif guess < secret:
        return -1
    elif guess == secret:
        return 0

def findNum():
    guess = 1
    if secretNum(guess) == 0:
        return guess
    foundFlag = True
    while foundFlag:
        sign = secretNum(guess)
        if sign == -1:
            guess *= 2
        elif sign == 1:
            guess -= 1
        elif sign == 0:
            return guess

print findNum()
