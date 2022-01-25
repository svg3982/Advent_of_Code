import numpy as np
import regex as re
import matplotlib.pyplot as plt
import itertools, collections

fish = []
with open('dec6_input.txt') as ip:
    for line in ip:
        line = line.replace("\n", "")
        fishys = line.split(",")
        fish = list(map(int, fishys))
ip.close()

first_fish = np.asarray(fish,dtype=np.uint16)
day = 0

"""while day < 80:
    #new = np.zeros(len(first_fish))
    #print("Day:", day, "Fish:", fish)
    for count, f in enumerate(first_fish):
        new_days = f-1
        if new_days == -1:
            first_fish[count] = 6
            first_fish = np.append(first_fish,8) #newfish
            continue
        first_fish[count] = (f-1)
    day += 1"""
#print len(first_fish)

fish = dict().fromkeys([i for i in range(9)], 0)
for i in first_fish:
    fish[i] += 1

while day < 256:
    will_spawn = fish[0]
    for days_left in range(1,9):
        fish[days_left-1] = fish[days_left]
    fish[8] = will_spawn
    fish[6] += will_spawn
    day += 1

print(sum(list(fish.values())))

def print_growth(fishes):
    years=np.arange(0,80)
    plt.plot(years, [sum(x) for x in fishes])
    plt.title("Growth rate of lanternfish")
    plt.ylabel("(Fish)")
    plt.xlabel("(Days)")
    plt.show()
