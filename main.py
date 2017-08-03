from functions.localmax import take_points
from mytest import readpds
from spice.spicesync import *

a=take_points('richy',2,1)
print (a, type(a))

readpds('test.IMG')

