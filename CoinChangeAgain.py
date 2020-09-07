import math

money = int(input())
denominations = [1, 3, 4]
minCoins = [0] + [math.inf]*money
print(minCoins)
for i in range(1, money+1):
    for j in denominations:
        print('i:',i)
        print('j:',j)
        if i>=j:
            coins = minCoins[i-j]+1
            print('coins:',coins)
            if coins < minCoins[i]:
                minCoins[i] = coins
            print(minCoins)
        else:
            break


print(minCoins[money])
