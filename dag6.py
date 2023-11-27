#!python3
import os
import datetime
import re
from collections import deque

# Test input
input = [3,4,3,1,2]

# input integers separated by commas
input= [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
#input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def day(fishies:deque):
    fishies.append(fishies[0])
    fishies[7] += fishies[0]
    fishies.popleft()

def solve1():
    for i in range(80):
        day(ages1)

    result = sum([a for a in ages1])
    print("Deel 1: " + str(result))

def solve2():
    for i in range(256): # 256 - 18
        day(ages2)

    result = sum([a for a in ages2])
    print("Deel 2: " + str(result))

ages1 = deque([0,0,0,0,0,0,0,0,0]) 
ages2 = deque([0,0,0,0,0,0,0,0,0])
for i in input:
    ages1[i] += 1
    ages2[i] += 1

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)


from collections import Counter
F = Counter([int(n) for n in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt', encoding="utf-8").read().split(",")])
start = datetime.datetime.now()
for day in range(256):
    new, FNext = F[0], {i: F[(i + 1) % 9] for i in range(9)}
    FNext[6] += new
    F = FNext
    if day + 1 == 80:
        print("Answer A:", sum(F.values()))
print("Answer B:", sum(F.values()))

print("Tijd voor oplossing Jan: ", datetime.datetime.now()-start)
