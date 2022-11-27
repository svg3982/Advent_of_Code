import numpy as np
import pandas

heights = np.loadtxt("dec9_test_input.txt",dtype=str)
heights_columns = np.genfromtxt("dec9_test_input.txt",dtype=str,delimiter=1)
print(heights_columns[:,0])

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

basin_sizes = []
# loop through points to calculate size of each basin
for row in min_positions_rows:
    for point in min_positions_rows.get(row):
        print(row,point)
        #find 9s in current row
        row_no = int(row)
        full_string = heights[row_no]
        left_limit = full_string.rfind("9", 0, point)
        right_limit = full_string.find("9", point)
        if right_limit == -1: right_limit = len(full_string) #find() puts -1 if not found
        basin_width = range(left_limit+1, right_limit)
        basin_temp = 0
        #find 9s in column
        for count,i in enumerate(basin_width):
            col = heights_columns[:,i] #row_no = current row
            if row_no == 0: upper_limit = 0
            else: 
                stop = np.where(col[:row_no] == "9")
                if any(map(len, stop)): #check whether stop (tuple) is not empty
                    upper_limit = stop[0][-1]+1
                else: 
                    upper_limit = len(heights)
            if row_no == len(heights)-1: lower_limit = len(heights) 
            else: 
                stop = np.where(col[row_no:] == "9")
                if any(map(len, stop)):
                    lower_limit = (row_no + stop[0][0])
                else:
                    lower_limit = len(heights) #might also be row_no... check
            basin_temp = basin_temp + (lower_limit - upper_limit)
            #find stragglers
        basin_sizes.append(basin_temp)
        print(basin_sizes)
        print(3+9+13+9)
        print(np.count_nonzero(heights_columns[:,:] == "9"))