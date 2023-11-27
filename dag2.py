#!python3
import os
import datetime
import re

# Test input
input = ["forward 5","down 5","forward 8","up 3","down 8","forward 2"]

# input integers separated by commas
#input= [int(i) for i in open("input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def solve1():
    direction_map = {"forward": ["x", 1], "down": ["z", 1], "up": ["z", -1]}
    position = {"x": 0, "y": 0, "z": 0}

    route = [(direction_map[x][0], int(y)*direction_map[x][1]) for x,y in [(i.split(" ")[0], i.split(" ")[1]) for i in input]]
    for r in route:
        position[r[0]] += r[1]
    print("Deel 1: " + str(position["x"]*position["z"]))

def solve2():
    position = {"x": 0, "y": 0, "z": 0}
    aim = 0
    for x,y in [(i.split(" ")[0], int(i.split(" ")[1])) for i in input]:
        if (x == 'forward'):
            position["x"] += y
            position["z"] += y * aim
        else:
            aim = aim + y if (x == 'down') else aim - y

    print("Deel 2: " + str(position["x"]*position["z"]))



start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
