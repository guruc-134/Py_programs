 import math 
equation=input("enter a quadratic equaion to find its roots\n")
terms=equation.split("+")
 a=int(terms[0][0])
b=int(terms[1][0])
c=int(terms[2])
variable=terms[1][1]
d=(b*b-4*a*c)
if d<0:
	print("this equation has imaginary roots")
	root1=(-b - math.sqrt(-d))/2*a
	root2=(-b + math.sqrt(-d))/2*a
	print(" the roots are :\n")
	print(" - %d - %di and - %d + %di"%(b/2*a,math.sqrt(-d)/2*a,b/2*a, math.sqrt(-d)/2*a))
elif d==0:
	print("this equation has equal roots")
	root1=(-b - math.sqrt(-d))/2*a
	root2=(-b + math.sqrt(-d))/2*a
	print(" the roots are :\n")
	print(" %d  and %d "%(root1,root2))
else :
	print("this equation has real and distinct roots")
	root1=(-b - math.sqrt(-d))/2*a
	root2=(-b + math.sqrt(-d))/2*a
	print(" the roots are :\n")
	print("%d and %d"%(root1,root2))

