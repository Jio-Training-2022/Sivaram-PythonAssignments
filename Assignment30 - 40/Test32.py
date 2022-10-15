import numpy as np
f = open("Arrayfile.txt", "r")
c = f.read()
c = c.split(' ')
arr = np.array(c)
print ("Array: ", arr)