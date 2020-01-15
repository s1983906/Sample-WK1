#find the minimum value

import numpy as np
from datetime import datetime

arr=np.random.random(100)
#j is remain of unordered array
#create sort algorithm
def minsort():
    minN=10000
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i:])):

            if arr[i] > arr[j+i]:
                t=arr[i]
                arr[i]=arr[j+i]
                arr[j+i]=t
            else:
                continue

    print(arr)
    return arr
#create a sort algorithm
minsort()
