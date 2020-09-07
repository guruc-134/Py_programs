""" denominations present are
1 5 10
"""
amount=int(input())
coinsNo=0
if amount <5:
    print(amount/1)
elif amount<10:
    rem=amount/5
    coinsNo=amount%5
    print(coinsNo)
else:
coin=[10,5,1]
for i in coin:
    coinsNo+=amount/i
    amount=amount%i
print(coinsNo)
