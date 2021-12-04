#!python3
import os
import datetime
import re
import copy

# Test input
input = [
"7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
"",
"22 13 17 11  0",
" 8  2 23  4 24",
"21  9 14 16  7",
" 6 10  3 18  5",
" 1 12 20 15 19",
"",
" 3 15  0  2 22",
" 9 18 13 17  5",
"19  8  7 25 23",
"20 11 10 24  4",
"14 21 16 12  6",
"",
"14 21 17 24  4",
"10 16 15  9 19",
"18  8 23 26 20",
"22 11 13  6  5",
" 2  0 12  3  7"
]

# input integers separated by commas
#input= [int(i) for i in open("input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def solve1():
    bingo = False
    boards1=copy.deepcopy(boards)
    for n in numbers:
        print(n)
        for b in boards1:
            for r in b["rows"]:
                if n in r: 
                    r.remove(n)
                    if len(r) == 0:
                        bingo = True
                        break
            for c in b["columns"]:
                if n in c:
                    c.remove(n)
                    if len(c) == 0:
                        bingo = True
                        break
            if bingo:
                result = sum([sum(r) for r in b["rows"]]) * n
                break
        if bingo:
            break

    print("Deel 1: " + str(result))

def solve2():
    bingo = set()
    boards2 = copy.deepcopy(boards)
    for n in numbers:
        print(n)
        for b in range(0, len(boards2)):
            for r in boards2[b]["rows"]:
                if n in r: 
                    r.remove(n)
                    if len(r) == 0:
                        bingo.add(b)
            for c in boards2[b]["columns"]:
                if n in c:
                    c.remove(n)
                    if len(c) == 0:
                        bingo.add(b)
            if len(bingo) == len(boards2):
                result = sum([sum(r) for r in boards2[b]["rows"]]) * n
                break
        if len(bingo) == len(boards2):
            break

    print("Deel 2: " + str(result))

numbers = [int(e) for e in input[0].split(",")]
boards = []
boardnum = 0
for l in range(2,len(input)-1,6):
    rawboard = []
    for line in range(l, l+5):
        rawboard.append([int(e) for e in input[line].split()])

    #boards.append({"rows": rawboard})
    columns = []
    for c in range(0,5):
        columns.append([rawboard[i][c] for i in range(0,5)])
    boards.append({"rows": rawboard, "columns": columns})
    #boards.append([int(e) [r for r in [input[line].split() for line in range(l,l+5)]]])

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
