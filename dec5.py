import numpy as np
import regex as re
import matplotlib.pyplot as plt
import itertools, collections

pairs = []
lines = []
with open('dec5_input.txt') as ip:
    for line in ip:
        line = line.replace("\n", "")
        start, end = line.split(" -> ")
        x1, y1 = start.split(",")
        x2, y2 = end.split(",")
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        #if not (x1 == x2 or y1 == y2): continue
        if x1 == x2:
            trajectory = []
            step = 1 if y1 < y2 else -1
            for j in range(abs(y2-y1)):
                new_y1 = y1 + (step*j)
                trajectory.append((x1,new_y1))
            trajectory.append((x2,y2))
        if y1 == y2:
            trajectory = []
            step = 1 if x1 < x2 else -1
            for j in range(abs(x2-x1)):
                new_x1 = x1 + (step*j)
                trajectory.append((new_x1,y1))
            trajectory.append((x2,y2))
        if not (abs(x2-x1) == abs(y2-y1)): continue #to remove weird paths
        #diagonals
        if ((x1+y1)%2 == 0) and ((x2+y2)%2 == 0):
            trajectory = []
            step_x = 1 if x1 < x2 else -1
            step_y = 1 if y1 < y2 else -1
            new_y_range = abs(y2-y1)
            for count,j in enumerate(range(abs(x2-x1))):
                new_x1 = x1 + (step_x*j)
                new_y1 = y1 + (step_y*count)
                trajectory.append((new_x1,new_y1))
            trajectory.append((x2,y2))
        lines.append(trajectory)
        pairs.append([(x1,y1),(x2,y2)])
ip.close()

def print_diagram(pairs):
    plt.figure(figsize=(9,9))
    plt.xlim(0, 9)
    plt.ylim(0, 9)
    for i in pairs:
        x = i[:][0]
        y = i[:][1]
        plt.plot(x,y)
    plt.grid(True)
    plt.show()

counter = collections.Counter(itertools.chain(*lines))
print(collections.Counter(counter.values()))
