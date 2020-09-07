import numpy as np
A=np.arange(1,10).reshape(3,3)
B=np.arange(11,20).reshape(3,3)
C=A.dot(B)
print(A)
print("    +\n")
print(B)
print("  =\n")
print(C)
