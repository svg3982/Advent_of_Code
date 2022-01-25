import numpy as np
import regex as re

set_of_signals, set_of_outputs = [], []
with open('dec8_input.txt') as ip:
    for line in ip:
        lines = line.split("|")
        signals = lines[0].split(" ")
        set_of_signals.append(signals)
        output = lines[1].replace("\n", "")
        output = output.split(" ")
        set_of_outputs.append(output)
ip.close()

dict_of_digits = {2 : 1, 5:[2,3,5], 4 : 4, 6:[0,6,9], 3 : 7, 7 : 8}
dict_of_decode = {0:"abcefg", 1:"cf", 2: "acdeg", 3:"acdfg", 4:"bcdf", 5:"abdfg", 6:"abdefg", 7:"acf", 8:"abcdefg", 9:"abcdfg"}
#find all 10 unique signal patterns
#return 4 digit puzzle output
current_signals = set_of_signals[0]
current_outputs = set_of_outputs[0]
#for task 1: only count 1,4,7,8 in outputs
count = 0
for item in set_of_outputs:
    for j in item:
        if len(j) in [2, 4, 3, 7]:
            #digit = dict_of_digits[len(j)]
            #decoding_string = dict_of_decode[digit]
            count += 1
print("Task 1. Counted instances of 1,4,7,8:", count)

for entry in set_of_signals:
    for i in entry:
        if len(i) in [2, 4, 3, 7]:
            digit = dict_of_digits[len(i)]
            decoding_string = dict_of_decode[digit]
    #find configuration
