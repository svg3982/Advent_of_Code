import numpy as np

energy_levels = np.genfromtxt("dec11_input.txt",dtype=int,delimiter=1)
print(energy_levels)
mask = np.ones(energy_levels.shape, dtype=bool)

rows = len(energy_levels)
columns = len(energy_levels[0])
print("rows: ", rows, "columns: ", columns)

flashes = 0
def flash(r,c):
    global flashes
    flashes += 1
    mask[r][c] = False
    for adjacent_row in [-1,0,1]:
        for adjacent_column in [-1,0,1]:
            new_row = r + adjacent_row
            new_column = c + adjacent_column
            if 0<=new_row<rows and 0<=new_column<columns and mask[new_row][new_column]: #row > new_row because the difference is max 1
                energy_levels[new_row][new_column] += 1
                if energy_levels[new_row][new_column] >= 10:
                    flash(new_row,new_column)

t=0
while True:
    t += 1
    for row in range(rows):
        for column in range(columns):
            energy_levels[row][column] += 1
    for row in range(rows):
        for column in range(columns):
            if energy_levels[row][column] == 10 and mask[row][column]:
                flash(row,column)
    synchronized = True #when mask is completely False
    #print(t, mask)
    for row in range(rows):
        for column in range(columns):
            if not mask[row][column]:
                energy_levels[row][column] = 0
                mask[row][column] = True
            else:
                synchronized = False
    #print(energy_levels)
    #print("time and flashes: ", t, flashes)
    if synchronized:
        print(t)
        print(mask)
        break
print(flashes)
