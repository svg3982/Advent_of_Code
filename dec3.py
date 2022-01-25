import numpy as np
import regex as re

numbers = []
nrs = re.compile('[0-9]+')
with open('dec3_input.txt') as ip:
    for line in ip:
        step = nrs.findall(line)[0]
        numbers.append(step)
ip.close()

print(numbers)

def count_position(binary_list,position):
    count_0 = 0
    count_1 = 0
    for i in binary_list:
        byte = i[position]
        if byte == '0':
            count_0 += 1
        if byte == '1':
            count_1 += 1
    return count_0, count_1

length_string = len(numbers[0])

def get_new_criteria(current_set):
    oxygen_criteria = ''
    CO2_criteria = ''
    gamma_rate = '' #most common bit in the corresponding position
    epsilon_rate = '' #least common bit from each position
    for j in range(length_string):
        count_0, count_1 = count_position(current_set,j)
        if count_0 > count_1:
            gamma_rate += '0'
            epsilon_rate += '1'
            oxygen_criteria += '0'
            CO2_criteria += '1'
        if count_1 > count_0:
            gamma_rate += '1'
            epsilon_rate += '0'
            oxygen_criteria += '1'
            CO2_criteria += '0'
        if count_0 == count_1:
            oxygen_criteria += '1'
            CO2_criteria += '0'
    return gamma_rate, epsilon_rate, oxygen_criteria, CO2_criteria
#print(int(gamma_rate,2),int(epsilon_rate,2),(int(epsilon_rate,2)*int(gamma_rate,2)))

def get_valid_nrs(binary_list,bit_criterion,starting_bit):
    current_regex = re.compile('^'+bit_criterion)
    new_list = []
    indices = []
    for count, nr in enumerate(binary_list):
        from_starting_bit = nr[starting_bit:]
        match = current_regex.match(from_starting_bit)
        if match:
            new_list.append(nr)
            indices.append(count)
    #temp_string = ''.join(binary_list)
    #print(temp_string)
    #selections = [(m.start(0), m.end(0)) for m in current_regex.finditer(temp_string)]
    #for count,j in enumerate(binary_list):
    print(new_list, indices)
    return new_list, indices

def get_rating(set_of_numbers, rating_type):
    _,_, oxygen_criteria, CO2_criteria = get_new_criteria(set_of_numbers)
    for bit_count in range(length_string):
        current_rating = oxygen_criteria if rating_type == "oxygen" else CO2_criteria
        print("The current bit count:", bit_count)
        print("The current rating's bit criterion:", current_rating[bit_count])
        corrected_set, indices = get_valid_nrs(set_of_numbers,current_rating[bit_count],bit_count)
        if len(corrected_set) == 1:
            print(corrected_set[0], "This is the", rating_type, "rating value for bit criterion", current_rating[bit_count])
            return corrected_set[0]
            break
        set_of_numbers = corrected_set
        _,_, oxygen_criteria, CO2_criteria = get_new_criteria(set_of_numbers)
        print("The current", rating_type,"criterion:", oxygen_criteria)

set_oxygen_rating = get_rating(numbers,"oxygen")
set_CO2_rating = get_rating(numbers,"CO2")

print(int(set_oxygen_rating,2),int(set_CO2_rating,2),(int(set_oxygen_rating,2)*int(set_CO2_rating,2)))
