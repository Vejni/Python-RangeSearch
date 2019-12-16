# Set up, run it to measure time
import matplotlib.pyplot as plt
import numpy as np
import timeit
from mpl_toolkits.mplot3d import Axes3D
from itertools import repeat


sizes = [10, 100, 200, 300]
ls = [s for item in sizes for s in repeat(item,4)]
qs = [s for s in sizes] * 4

# Task21
import Task21 as t
import time

task21_times = []

def code_to_test():
    mylist = []
    
    for i in l:
        t.add_new_numbers(mylist, i)
        
    for element in mylist:
        element = t.Node(element)

    t.create_next_level(t.Node.getnodes())
    root = t.Node.getroot()
        
    for q in qs:
        t.query(root, min(q), max(q))
        print(".",end=" ")

for s1 in sizes:
    l = np.random.randint(low=0, high=100000, size=(s1))
    for s2 in sizes:
        qs = np.random.randint(low=0, high=100000, size=(s2,2))
        now = time.time()
        
        code_to_test()
        
        elapsed_time = time.time() - now
        task21_times.append(elapsed_time)
        print (elapsed_time)