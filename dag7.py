#!python3
import os
import datetime

# Test input
input = [16,1,2,0,4,2,7,1,2,14]

# input integers separated by commas
input= [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
#input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()


def solve1():
    dist = {}
    for p in range(min(input), max(input)+1):
        dist[p] = sum([abs(i-p) for i in input])
    #print(dist)
    result = min(dist.values())
    print("Deel 1: " + str(result))

def solve2():
    dist = {}
    for p in range(min(input), max(input)+1):
        dist[p] = sum([sum(range(1,abs(i-p)+1)) for i in input])
    #print(dist)
    result = min(dist.values())
    print("Deel 2: " + str(result))


start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)

