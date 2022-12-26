import random
import string
t = int(input("Введите кол-во строк:"))
if (t>=1) and t<=100:
    for i in range(t):
        s = random.randint(1,100)
        symbols = '01'
        randstr = ''.join(random.choice(symbols)for z in range(s))
        print(randstr)
        print(randstr.strip('0').count('0'))
else:
    print('Error!')
