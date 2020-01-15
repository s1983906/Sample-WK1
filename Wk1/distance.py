#find the minimum value

import numpy as np

def findmini():
    arr=np.random.random(100)

    minval=arr[0]
    maxval=arr[0]
    for i in arr:
        if i<minval:
            minval=i
            if i > maxval:
                maxval=i

                print (findfini)
