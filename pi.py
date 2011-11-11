#!/usr/bin/env python

from random import uniform as random
from math import pi
from time import time

r = 1
num_of_points = 10000000

def get_point():
    return (random(-r,r), random(-r,r))

def in_a_circle(point):
    return r**2 >= point[0]**2 + point[1]**2

start = time()
mypi = 4.0 * float(len(filter(in_a_circle, (get_point() for i in xrange(num_of_points))))) / float(num_of_points)
end = time()

print "calculated value of pi: %f" % mypi
print "done in %f seconds" % (end-start)
print "pi value from math lib: %f" % pi
