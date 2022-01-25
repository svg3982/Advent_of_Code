import numpy as np
import regex as re

vect = []
nrs = re.compile('[0-9]+')
with open('dec1_input.txt') as ip:
    for line in ip:
        new_line = nrs.findall(line)[0]
        vect.append(int(new_line))
ip.close()

''' increase = 0
start = vect[0]
for i in vect:
    if i > start:
        increase += 1
    start = i '''

#a three measurement sliding window
increase = 0
previous_window = vect[0:3]
for i in vect:
    previous_sum = sum(previous_window)
    current_window = [previous_window[1],previous_window[2],i]
    current_sum = sum(current_window)
    if current_sum > previous_sum:
        increase += 1
    previous_window = current_window
print(increase)
