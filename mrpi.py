#!/usr/bin/env python

from random import random
from math import pi
from multiprocessing import Pool
from time import time

# Assume radius equals 1
num_of_points = 1000000
num_of_workers = 2
real_number_of_points = num_of_points/num_of_workers*num_of_workers

def get_point():
    return (random(), random())

def in_circle(point):
    return 1 >= point[0]**2 + point[1]**2

def generate_points(x):
    return [get_point() for i in xrange(x)]

def get_those_in_circle(x):
    return filter(in_circle, x)

if __name__ == "__main__":
    workers = Pool(processes=num_of_workers)

    start = time()
    points = workers.map(generate_points,
            (real_number_of_points/num_of_workers
                for i in xrange(num_of_workers)))
    points_in_circle = workers.map(get_those_in_circle, points)
    num_of_points_in_circle = workers.map(len, points_in_circle)
    num_of_points_in_circle = reduce(lambda x,y: x+y, num_of_points_in_circle)

    mypi = float(num_of_points_in_circle) / float(real_number_of_points) * 4.0
    end = time()

    print "calculated value of pi: %f" % mypi
    print "done in %f seconds" % (end-start)
    print "pi value from math lib: %f" % pi
