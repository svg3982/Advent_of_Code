import numpy as np
import re
from collections import deque

navigation = np.loadtxt("dec10_input.txt",dtype=str)
mask = np.ones(len(navigation), dtype=bool)
print(navigation)

openingBrackets = ['(','[',"{","<"]
closingBrackets = [')',']',"}",">"]
chunks = {"(":")","[":"]","{":"}","<":">"}
#scoring = {")":3,"]":57,"}":1197,">":25137} #for task 1
scoring = {")":1,"]":2,"}":3,">":4}
scoreboard = []

def check_corruption(line):
    stack = deque()
    for character in line:
        if character in openingBrackets:
            stack.append(character)
        elif character in closingBrackets:
            matching_opener = stack.pop()
            if chunks[matching_opener]!=character:
                #scoreboard[line] = scoring[character] #for task 1
                return True
    return False

def complete(line):
    stack = deque()
    closer = ""
    score = 0
    for character in line:
        if character in openingBrackets:
            stack.append(character)
        elif character in closingBrackets:
            stack.pop()
    for j in range(len(stack)):
        opener = stack.pop()
        matching_closer = chunks[opener]
        closer += matching_closer
        score = (score*5) + scoring[matching_closer]
    return(closer,score)

for count,i in enumerate(navigation[:]):
    if check_corruption(i): 
        mask[count] = False #remove corrupted lines
leftovers = navigation[mask]
#complete remaining lines
for i in leftovers:
    closer, score = complete(i)
    scoreboard.append(score)
    print("line: ",i,"closer: ", closer)
#print scores
print(scoreboard)
print(int(np.median(np.sort(scoreboard))))