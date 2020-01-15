#chessboard with squares from [0,0] to [8,8]
from math import sqrt

#want distance btw
for x0 in range (1,9):
    for y0 in range (1,9):
        # point1 (x0, y0)
        for x1 in range(1,9):
            for y1 in range (1,9):


                    distance=sqrt((x1-x0)**2+(y1-y0)**2)
                    print (x,y)
