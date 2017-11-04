# generator
# list_prime = [2,3,5,7,11]
def genPrimes():
    # global list_prime
    list_prime = [2]
    n = list_prime[-1]
    flag = True
    while True:
        for num in list_prime[:-1]:
            if n % num == 0:
                flag = False
                break

        if flag:
            list_prime.append(n)
            yield n

        flag = True
        n += 1

k = genPrimes()
print k.next()
print k.next()
print k.next()
print k.next()
print k.next()
