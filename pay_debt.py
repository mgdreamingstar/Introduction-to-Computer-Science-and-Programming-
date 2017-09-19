annualInterestRate = 0.18
balance = [5000]

monthly = 1000
unbalance = []

for i in range(1,13):
    unbalance.append(balance[i-1] - monthly)
    balance.append(unbalance[i-1] * (1 + annualInterestRate / 12.0))
    print 'balance %d = %d' %(i,balance[i])
