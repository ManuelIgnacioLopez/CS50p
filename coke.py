# coke machine money calculator
# coins accepted: 5, 10, 25
coins =[5,10,25]
owed = 50
while owed>0:
    print(f'Amount Due: {owed}')
    coin=input('Insert Coin: ')
    coin=int(coin)
    if coin in coins:
        owed-=coin

print(f'Change Owed: {-1*owed}')