import re
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np

file = open("W20150511T083550851ID30F18.txt", "r+")
file2 = open("W20150511T100357791ID30F18.txt", "r+")

x1 =[]
y1 =[]
for lines in file:
    x = re.findall('.*,', lines)
    x = x[0][0:-1]
    x1.append(x)
    y = re.findall(',.*\n', lines)
    y = y[0][1:-1]
    y1.append(y)

if len(x1) != len(y1):
    print ('ERROR: not possible set of data')

if len(x1) == len(y1):
    print ('lets continue')

x2 =[]
y2 =[]
for lines in file2:
    x = re.findall('.*,', lines)
    x = x[0][0:-1]
    x2.append(x)
    y = re.findall(',.*\n', lines)
    y = y[0][1:-1]
    y2.append(y)

if len(x2) != len(y2):
    print ('ERROR: not possible set of data')

if len(x2) == len(y2):
    print ('lets continue')

plt.subplot(111)
#ax=plt.subplot(111)

a,= plt.plot(x1, y1, '+', label="Initial positions", color= 'salmon')
b,= plt.plot(x2, y2, '+', label="Final Positions", color='teal')



plt.title("Dust trajectories")
plt.ylabel('y pixels')
plt.xlabel('x pixels')
plt.legend(handles=[a, b])

plt.show()
print('done')