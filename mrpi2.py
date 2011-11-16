#!/usr/bin/env python

from random import random
from math import pi
from multiprocessing import Pool
from time import time

# Assume radius equals 1
num_of_points = 1000000
num_of_workers = 2
points_per_worker = num_of_points/num_of_workers
real_number_of_points = points_per_worker*num_of_workers

def perform_an_experiment(experiment_num_of_points):
    in_a_circle = lambda point: 1 >= point[0]**2 + point[1]**2
    return sum(
            (
                in_a_circle((random(), random()))
                for i in xrange(experiment_num_of_points)
            )
            )

workers = Pool(processes=num_of_workers)

start = time()
num_of_points_in_circle = workers.map(perform_an_experiment,
        (points_per_worker for i in xrange(num_of_workers)))
num_of_points_in_circle = reduce(lambda x,y: x+y, num_of_points_in_circle)

mypi = float(num_of_points_in_circle) / float(real_number_of_points) * 4.0
end = time()

print "calculated value of pi: %f" % mypi
print "done in %f seconds" % (end-start)
print "pi value from math lib: %f" % pi
