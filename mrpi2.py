#!/usr/bin/env python

from random import uniform as random
from math import pi
from multiprocessing import Pool
from time import time

r = 1
num_of_points = 10000000
num_of_workers = 2
real_number_of_points = num_of_points/num_of_workers*num_of_workers

def get_point():
    return (random(-r, r), random(-r,r))

def in_circle(point):
    return r**2 >= point[0]**2 + point[1]**2

def perform_an_experiment(experiment_num_of_points):
    return len(filter(in_circle,
        (get_point() for i in xrange(experiment_num_of_points))))

workers = Pool(processes=num_of_workers)

start = time()
num_of_points_in_circle = workers.map(perform_an_experiment,
        (real_number_of_points/num_of_workers for i in xrange(num_of_workers)))
num_of_points_in_circle = reduce(lambda x,y: x+y, num_of_points_in_circle)

mypi = float(num_of_points_in_circle) / float(real_number_of_points) * 4.0
end = time()

print "calculated value of pi: %f" % mypi
print "done in %f seconds" % (end-start)
print "pi value from math lib: %f" % pi
