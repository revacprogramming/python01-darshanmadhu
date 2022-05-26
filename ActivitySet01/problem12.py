 
import re     
hand = open("regex_sum_340267.txt", "r")
numlist = []      
for line in hand:
    line = line.rstrip()
    integers = re.findall('([0-9]+)', line)   
    for number in integers: numlist.append(int(number))            an
                                 