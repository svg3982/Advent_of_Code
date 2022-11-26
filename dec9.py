import numpy as np
import pandas

heights = np.loadtxt("dec9_test_input.txt",dtype=str)
heights_p = pandas.read_csv("dec9_test_input.txt", dtype=str, header=None)

heights_p = pandas.DataFrame([list(x) for x in heights_p[0]])
print(heights_p)

def check_up_down(value, position,row):
    if row == 0: up = 9
    else: up = int(heights[row-1][position])
    if row == len(heights)-1: down = 9
    else: down = int(heights[row+1][position])
    if value < up and value < down:
        return True
    return False

#find minimum in each row; check left, check right
min_positions_rows = {}
risks = []
for row,location in enumerate(heights): #loop through every line in input file (1 line = location)
    left = 9
    right = 9
    for position,height_value in enumerate(location): #keep position & value separate
        #update values on the left & the right, for comparison
        current = int(height_value)
        if position == len(location)-1:
            right = 9
        else: 
            right = int(location[position+1])
        if current < left and current < right:
            vertical = check_up_down(int(height_value),position,row) #check up & down 
            dict_key = str(row) #row number as key, in string format
            if dict_key in min_positions_rows and vertical is True:
                min_positions_rows[dict_key].append(position)
                risks.append(1+int(height_value))
            elif vertical is True:
                min_positions_rows.update({dict_key:[position]})
                risks.append(1+int(height_value))
        left = current
print(sum(risks))
