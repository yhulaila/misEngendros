import numpy as np
from parsing import readpds

image = readpds('../test.IMG')

arr = np.zeros((1,2048,2048))

print (image.shape)
print (image[0,0,0])
print (image[0,1,0])
print (image[0,2,0])
print (image[0,0,1])
print (image[0,0,2])
print (image[0,1,1])

img2 = np.empty((2048, 2048))
for i in range(0, len(image[0, 0])):
    for j in range(0, len(image[0, 0])):
        img2[i, j] = image[0, i, j]

print (img2.shape)
print (img2[0,0])
print (img2[1,0])
print (img2[2,0])
print (img2[0,1])
print (img2[0,2])
print (img2[1,1])



arr[0,2047,2047]=1
print(arr)
for i in range(0,len(arr[0,0])):
    for j in range(0, len(arr[0, 0])):
        if arr[0,i,j]==1:
            print ('valor encontrado en índice (0, ', i,',',j,  ') con valor', arr[0,i,j])

