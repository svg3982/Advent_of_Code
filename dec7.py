import numpy as np
import regex as re
import matplotlib.pyplot as plt
import itertools, collections

pos = []
with open('dec7_input.txt') as ip:
    for line in ip:
        line = line.replace("\n", "")
        positions = line.split(",")
        pos = list(map(int, positions))
ip.close()

leftmost = min(pos)
rightmost = max(pos)
possible_positions = np.arange(leftmost, rightmost) #full range of possible options
options = np.ones(len(possible_positions)) #keep track of winners
fuel_costs = dict().fromkeys([i for i in possible_positions],0)
different_positions = set(pos) #unique horizontal positions
crabs = dict().fromkeys([i for i in different_positions],0)
#fill loop with: horiz_position: # of crabs
for i in pos:
    crabs[i] += 1
min_indicator = 1*10^6
for index, possibility in enumerate(possible_positions):
    if options[index] == 0: # useless
        continue
    for item in crabs:
        #fuel = abs(item - possibility) #costs of movement for part 1
        steps = abs(item - possibility)
        fuel = int(steps*(steps+1)/2) #costs of movement for part 2: Triangular numbers
        fuel_costs[possibility] += (fuel*crabs[item]) #multiply by number of crabs here
        if fuel_costs[possibility] >= min_indicator: #loser
            options[index] = 0
            continue
    if fuel_costs[possibility] <= min_indicator:
        min_indicator = fuel_costs[possibility]

cheapest = min(fuel_costs, key=fuel_costs.get)
print("Cheapest position:", cheapest, "Fuel necessary:", fuel_costs[cheapest])
