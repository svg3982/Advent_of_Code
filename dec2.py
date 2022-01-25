import numpy as np
import regex as re

moves = []
steps = []
move = re.compile('[a-z]+')
nrs = re.compile('[0-9]+')
with open('dec2_input.txt') as ip:
    for line in ip:
        current_move = str(move.findall(line)[0])
        step = int(nrs.findall(line)[0])
        moves.append(current_move)
        steps.append(step)
ip.close()

horiz_pos = 0
depth_pos = 0
aim = 0

'''
horiz_moves = np.where(np.asarray(moves)=='forward')
horiz_steps = np.asarray(steps)[horiz_moves]
horiz_pos = sum(horiz_steps)

up_moves = np.where(np.asarray(moves)=='up')
up_steps = np.asarray(steps)[up_moves]
down_moves = np.where(np.asarray(moves)=='down')
down_steps = np.asarray(steps)[down_moves]

#depth_pos = sum(down_steps) - sum(up_steps)
#print(horiz_pos, depth_pos)
#print(horiz_pos*depth_pos)
'''

for count,item in enumerate(moves):
    current_move = item
    current_step = steps[count]
    if current_move == 'forward':
        horiz_pos += current_step
        depth_pos += aim * current_step
    if current_move == 'up':
        aim -= current_step
    if current_move == 'down':
        aim += current_step
print(horiz_pos, aim, depth_pos)
print(horiz_pos*depth_pos)
