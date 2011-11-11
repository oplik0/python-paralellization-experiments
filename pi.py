#!/usr/bin/env python

from random import random
from math import pi
from time import time

# Assume that radius equals 1.
num_of_points = 10000000

in_a_circle = lambda point: 1 >= point[0]**2 + point[1]**2

start = time()
mypi = 4.0\
       * sum((in_a_circle((random(), random())) for i in xrange(num_of_points)))\
       / float(num_of_points)
end = time()

print "calculated value of pi: %f" % mypi
print "done in %f seconds" % (end-start)
print "pi value from math lib: %f" % pi
