import copy
annualInterestRate = 0.18
balance = [5000]

def lowest(b,a):

    balance = copy.deepcopy(b)
    annualInterestRate = a

    low = 0
    high = balance[0]
    monthly = balance[0] / 2
    unbalance = []
    balance_negative = 0

    while True:
        balance = copy.deepcopy(b)
        unbalance = []
        for i in range(1,13):
            unbalance.append(balance[i-1] - monthly)
            balance.append(unbalance[i-1] * (1 + annualInterestRate / 12.0))
            # print 'balance %d = %d' %(i,balance[i])

        balance_negative = sum([i < 0 for i in balance])

        if balance_negative == 0:
            low = monthly
        elif balance_negative >= 2:
            high = monthly
        elif abs(balance[-1]) < 100:
            return monthly
        else:
            print('wrong')
            low = monthly

        monthly = (low + high) / 2
        print(balance[-1], balance_negative)
lowest(balance, annualInterestRate)
