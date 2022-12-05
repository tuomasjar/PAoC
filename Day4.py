#! /usr/bin/env python

file = open("day4Input.txt","r")
lines = file.readlines()
sum = 0
for line in lines:
    elves = line.split(",")
    elf1 = elves[0].split("-")
    elf2 = elves[1].split("-")
    if(int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1])):
        sum += 1
    elif(int(elf2[0]) >= int(elf1[0]) and int(elf2[1]) <= int(elf1[1])):
        sum+=1
print("Solution 1: {}".format(sum))
sum = 0
for line in lines:
    elves = line.split(",")
    elf1 = elves[0].split("-")
    elf2 = elves[1].split("-")
    if(int(elf1[0]) >= int(elf2[0]) and int(elf1[0]) <= int(elf2[1])):
        sum += 1
    elif(int(elf2[0]) >= int(elf1[0]) and int(elf2[0]) <= int(elf1[1])):
        sum+=1
    elif(int(elf1[1]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1])):
        sum += 1
    elif(int(elf2[1]) >= int(elf1[0]) and int(elf2[1]) <= int(elf1[1])):
        sum+=1
print("Solution 2: {}".format(sum))