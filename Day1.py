#! /usr/bin/env python

file = open("day1Input.txt","r")
lines = file.readlines()
sum = 0
max = 0

for line in lines:
    if(line.strip().isnumeric()):
        sum += int(line)
    else:
        if(sum > max):
            max = sum
        sum = 0
            
            
print("Part 1: {}".format(max))

file = open("day1Input.txt","r")
lines = file.readlines()
sum = 0
max1 = 0
max2 = 0
max3 = 0

for line in lines:
    if(line.strip().isnumeric()):
        sum += int(line)
    else:
        if(sum > max1):
            max3 = max2
            max2 = max1
            max1 = sum
        elif(sum > max2):
            max3 = max2
            max2 = sum
        elif(sum > max3):
            max3 = sum
        sum = 0

max = max1 + max2 + max3

print("Part 2: {}".format(max))