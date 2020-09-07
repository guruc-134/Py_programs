n=int(input('enter a year'))
b=False
if n% 400==0:
    b=True

elif n%100==0:
    b=False

elif n%4==0:
    b=True

if b== True:
    print("leap")
