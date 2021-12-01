#!python3
import os
import datetime
import re

# Test input
input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

# input integers separated by commas
#input= [int(i) for i in open(os.path.basename(__file__).split(".")[0]+'.input').read().split(",")]

# input integers on complete lines
input = [int(i) for i in open(os.path.basename(__file__).split(".")[0]+'.input').read().splitlines()]

# input complete lines
#input = open(os.path.basename(__file__).split(".")[0]+'.input').read().splitlines()

def solve1():
    pluses = 0
    for i in range(1,len(input)):
        if (input[i]>input[i-1]):
            pluses += 1
    print("Deel 1: " + str(pluses))

def solve2():
    pluses = 0
    for i in range(3,len(input)):
        if (input[i]+input[i-1]+input[i-2] > input[i-1]+input[i-2]+input[i-3]):
            pluses += 1
    print("Deel 2: " + str(pluses))

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
