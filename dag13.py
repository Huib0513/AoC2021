#!python3
import os
import datetime
from collections import defaultdict

# Test input
input = [
"6,10",
"0,14",
"9,10",
"0,3",
"10,4",
"4,11",
"6,0",
"6,12",
"4,1",
"0,13",
"10,12",
"3,4",
"3,0",
"8,4",
"1,10",
"2,14",
"8,10",
"9,0",
"",
"fold along y=7",
"fold along x=5"
]

# input integers separated by commas
#input= [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
#input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def solve1():
    kaart = defaultdict(lambda: defaultdict(int))
    folds = []

    for l in input:
        if (len(l)):
            if l[0].isdigit():
                kaart[int(l.split(",")[1])][int(l.split(",")[0])] = 1
            else:
                folds.append((l.split()[2].split('=')[0], l.split()[2].split('=')[1]))
                continue

    for o,n in folds:
        if (o == 'y'):
            tofold = kaart[n:]
            for fr in range(len(tofold)-1):
                kaart[n-fr] = [kaart[n-fr][x] for x in fr.keys()]
        else:
            continue
    result = "No"
    print("Deel 1: " + str(result))

def solve2():
    result = "No"
    print("Deel 2: " + str(result))


start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
