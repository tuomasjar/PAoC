#! /usr/bin/env python
file = open("day6Input.txt","r")
lines = file.readlines()[0]
result = 0
checked = []
for i in range(3,len(lines)):
    found = True
    checked.clear()
    for j in range(3,-1,-1):
        if lines[i-j] in checked:
            found = False
            break
        else:
            checked.append(lines[i-j])
    if found==True:
        result = i+1
        break
print("Solution is: {}".format(result))

file = open("day6Input.txt","r")
lines = file.readlines()[0]
result = 0
checked = []
for i in range(13,len(lines)):
    found = True
    checked.clear()
    for j in range(13,-1,-1):
        if lines[i-j] in checked:
            found = False
            break
        else:
            checked.append(lines[i-j])
    if found==True:
        result = i+1
        break
print("Solution is: {}".format(result))