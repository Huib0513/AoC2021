#!python3
import os
import datetime
import re
from collections import defaultdict

# Test input
input = [
"0,9 -> 5,9",
"8,0 -> 0,8",
"9,4 -> 3,4",
"2,2 -> 2,1",
"7,0 -> 7,4",
"6,4 -> 2,0",
"0,9 -> 2,9",
"3,4 -> 1,4",
"0,0 -> 8,8",
"5,5 -> 8,2"
]

# input integers separated by commas
#input= [int(i) for i in open("input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def inclusive_range(start, stop, step):
    return range(start, (stop + 1) if step >= 0 else (stop - 1), step)

def solve1():
    kaart = defaultdict(int)

    for (start,end) in [(line.split(" -> ")[0], line.split(" -> ")[1]) for line in input]:
        startx,starty = int(start.split(",")[0]), int(start.split(",")[1])
        endx,endy = int(end.split(",")[0]), int(end.split(",")[1])

        if (startx == endx):
            for y in range(min(starty,endy), max(starty, endy)+1):
                #print(startx, y)
                kaart[startx,y] += 1
        elif (starty == endy):
            for x in range(min(startx,endx), max(startx, endx)+1):
                #print(x, starty)
                kaart[x,starty] += 1

    result = (len([v for v in kaart.values() if v>1]))
    print("Deel 1: " + str(result))

def solve2():
    kaart = defaultdict(int)

    for (start,end) in [(line.split(" -> ")[0], line.split(" -> ")[1]) for line in input]:
        startx,starty = int(start.split(",")[0]), int(start.split(",")[1])
        endx,endy = int(end.split(",")[0]), int(end.split(",")[1])

        if (startx == endx):
            for y in range(min(starty,endy), max(starty, endy)+1):
                #print(startx, y)
                kaart[startx,y] += 1
        elif (starty == endy):
            for x in range(min(startx,endx), max(startx, endx)+1):
                #print(x, starty)
                kaart[x,starty] += 1
        else:
            for x,y  in zip(inclusive_range(startx, endx, 1 if (endx>startx) else -1),inclusive_range(starty,endy, 1 if (endy>starty) else -1)):
                #print(x,y)
                kaart[x,y] += 1

    result = (len([v for v in kaart.values() if v>1]))
    print("Deel 2: " + str(result))


start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
