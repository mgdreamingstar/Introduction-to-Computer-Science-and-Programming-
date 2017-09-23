'''monthly % 10 == 0 每月付的钱应是10的倍数。'''

import copy
balance = [5000]
annualInterestRate = 0.18

def pay_debt(ba,annual):


    monthly = 0
    maxiter = (ba[0] // 10) // 2

    while maxiter > 0:

        monthly += 10
        balance = copy.deepcopy(ba)
        unbalance = []

        for i in range(1,13):
            unbalance.append(balance[i-1] - monthly)
            balance.append(unbalance[i-1] * (1 + annual / 12.0))

        print(balance[-1], monthly)
        if balance[-1] > 0:
            continue
        elif balance[-1] < 0:
            return monthly

        maxiter -= 1

# pay_debt([3329],0.2)
# pay_debt([4773],0.2)
pay_debt([3926],0.2)
