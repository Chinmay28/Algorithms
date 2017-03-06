

for number in range(999995700, 999996000):
    flag = False
    for num in range(2, 10001):
        prime = True
        for i in range(2, num):
            if (num%i==0):
                continue
        if prime:
            if number%num == 0:
                flag = True
                print(number, num, flag)
                break
    
    if not flag:
        print(number)