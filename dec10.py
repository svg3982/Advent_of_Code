import numpy as np
import re
from collections import deque

navigation = np.loadtxt("dec10_test_input.txt",dtype=str)
mask = np.ones(len(navigation), dtype=bool)
print(navigation)

openingBrackets = ['(','[',"{","<"]
closingBrackets = [')',']',"}",">"]
chunks = {"(":")","[":"]","{":"}","<":">"}
scoring = {")":3,"]":57,"}":1197,">":25137}
scoreboard = {}

def check_corruption(line):
    stack = deque()
    for character in line:
        if character in openingBrackets:
            stack.append(character)
        elif character in closingBrackets:
            matching_opener = stack.pop()
            if chunks[matching_opener]!=character:
                scoreboard[line] = scoring[character]
                return True
    return False

for count,i in enumerate(navigation[:]):
    '''if len(i)%2 != 0:  #check length: if uneven, string is incomplete
        print("incomplete")
        continue'''
    if check_corruption(i): mask[count] = False #remove corrupted lines
leftovers = navigation[mask]
print(len(leftovers))
print(scoreboard)
print(sum(scoreboard.values()))