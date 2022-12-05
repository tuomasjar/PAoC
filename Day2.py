#! /usr/bin/env python

file = open("day2Input.txt","r")
lines = file.readlines()
points = 0
for line in lines:
    if(line[2]=="X"):
        points += 1
        if(line[0]=="A"):
            points+=3
        elif(line[0]=="B"):
            points+=0
        elif(line[0]=="C"):
            points+=6
    elif(line[2]=="Y"):
        points += 2
        if(line[0]=="A"):
            points+=6
        elif(line[0]=="B"):
            points+=3
        elif(line[0]=="C"):
            points+=0
    elif(line[2]=="Z"):
        points += 3
        if(line[0]=="A"):
            points+=0
        elif(line[0]=="B"):
            points+=6
        elif(line[0]=="C"):
            points+=3
print("Solution 1: {}".format(points))
points = 0
for line in lines:
    if(line[2]=="X"):
        points += 0
        if(line[0]=="A"):
            points+=3
        elif(line[0]=="B"):
            points+=1
        elif(line[0]=="C"):
            points+=2
    elif(line[2]=="Y"):
        points += 3
        if(line[0]=="A"):
            points+=1
        elif(line[0]=="B"):
            points+=2
        elif(line[0]=="C"):
            points+=3
    elif(line[2]=="Z"):
        points += 6
        if(line[0]=="A"):
            points+=2
        elif(line[0]=="B"):
            points+=3
        elif(line[0]=="C"):
            points+=1

print("Solution 2: {}".format(points))