#! /usr/bin/env python
#[S]                 [T] [Q]        
#[L]             [B] [M] [P]     [T]
#[F]     [S]     [Z] [N] [S]     [R]
#[Z] [R] [N]     [R] [D] [F]     [V]
#[D] [Z] [H] [J] [W] [G] [W]     [G]
#[B] [M] [C] [F] [H] [Z] [N] [R] [L]
#[R] [B] [L] [C] [G] [J] [L] [Z] [C]
#[H] [T] [Z] [S] [P] [V] [G] [M] [M]
# 1   2   3   4   5   6   7   8   9 



file = open("day5Input.txt","r")
lines = file.readlines()

stacks = [[""],["H","R","B","D","Z","F","L","S"], ["T","B","M","Z","R"], ["Z","L","C","H","N","S"],
          ["S","C","F","J"], ["P","G","H","W","R","Z","B"], ["V","J","Z","G","D","N","M","T"],
          ["G","L","N","W","F","S","P","Q"], ["M","Z","R"], ["M","C","L","G","V","R","T"]]

for line in lines:
    parts = line.split(" ")
    repeats = int(parts[1])
    source = int(parts[3])
    dest = int(parts[5])
    for i in range(repeats):
        stacks[dest].append(stacks[source].pop())
result = ""
for stack in range(1,10):
    result += stacks[stack].pop()
print("Solution 1: " + result)
stacks = [[""],["H","R","B","D","Z","F","L","S"], ["T","B","M","Z","R"], ["Z","L","C","H","N","S"],
          ["S","C","F","J"], ["P","G","H","W","R","Z","B"], ["V","J","Z","G","D","N","M","T"],
          ["G","L","N","W","F","S","P","Q"], ["M","Z","R"], ["M","C","L","G","V","R","T"]]
tempStack = []
for line in lines:
    parts = line.split(" ")
    repeats = int(parts[1])
    source = int(parts[3])
    dest = int(parts[5])
    for i in range(repeats):
        tempStack.append(stacks[source].pop())
    for i in range(repeats):
        stacks[dest].append(tempStack.pop())
    tempStack = []
result = ""
for stack in range(1,10):
    result += stacks[stack].pop()
print("Solution 2: " + result)