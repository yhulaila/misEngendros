import re
import matplotlib.pyplot as plt
import skimage.morphology as morph
import skimage.exposure as skie

route1 = 'data/W20150511T083550851ID30F18.IMG'
print(route1)
route2 = 'cache' + str(route1[4:31]) + '.txt'
print (route2)

file =  open('data/list2.txt')

file = file.readlines()
route =[]
for line in file:
    route.append('cache/'+line[0:26]+ '.txt')
array=[]
for i in range(0,len(route)):
    file = open(route[i])
    file = file.readlines()
    for line in file:
        array.append(line)

print(array[0], array[1])
print(len(array[0]),type(array[0]))
x=[]
y=[]
for set in array:
    tmp =  re.split(r",+", set)
    x.append(tmp[0])
    tmp2 = re.split(r"\n+", tmp[1])
    y.append(tmp2[0])

print ('x', len(x))
print ('y', len(y))

# Creating figure to show local maximum detection
# rate success
plt.plot([x],[y], marker='o', markersize=0.1, color= "black")
plt.show()