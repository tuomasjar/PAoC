#! /usr/bin/env python

file = open("day3Input.txt","r")
lines = file.readlines()
sum = 0
for line in lines:
    part1 = line[:int(len(line)/2)]
    part2 = line[int(len(line)/2):]
    for char in part1:
        if char in part2:
            if(ord(char)<ord('a')):
                sum += 27 + (ord(char)-ord('A'))
            else:
                sum += 1 + (ord(char)-ord('a'))
            break
print("Solution 1: {}".format(sum))

sum = 0
for index in range(0,len(lines),3):
    for char in lines[index]:
        if char in lines[index+1] and char in lines[index+2]:
            if(ord(char)<ord('a')):
                sum += 27 + (ord(char)-ord('A'))
            else:
                sum += 1 + (ord(char)-ord('a'))
            break
print("Solution 2: {}".format(sum))