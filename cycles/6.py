purchase = int(input(''))
a = 0
while purchase != 0:
    a = a + purchase
    purchase = int(input(''))
if a % 2 == 0:
    while a % 2 == 0:
        a = a // 2
else:
    a = a - a*0.15
print('Сумма к оплате:', a)
