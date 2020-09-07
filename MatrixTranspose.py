import numpy as np
a=[
     [1,2,3],
     [3,4,5],
     [5,6,7]
     ]
at=[[row[i] for row in a] for i in range(3)]
array=np.array(a)
arrTrans=np.array(at)
print(array)
print("\nthe transpose is\n")
print(arrTrans)
