price = float(input(''))
dsc = int(input(''))
sale = price - price*dsc/100
while price != 0:
    print(sale)
    if price == '0':
        break
    price = float(input(''))
