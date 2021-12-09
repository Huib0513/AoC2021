#!python3
import os
import datetime

# Test input
input = [
"2199943210",
"3987894921",
"9856789892",
"8767896789",
"9899965678"
]

# input integers separated by commas
#input= [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def solve1():
    result = 0
    kaart = []
    for y in range(len(input)):
        for x in range(len(input[y])):
            candidate = False
            if (x ==0):
                if (input[y][x] < input[y][x+1]):
                    candidate = True
            elif (x == len(input[y])-1):
                if (input[y][x] < input[y][x-1]):
                    candidate = True
            else:
                if ((input[y][x] < input[y][x-1]) and (input[y][x] < input[y][x+1])):
                    candidate = True
            if (candidate):
                if (y ==0):
                    if (input[y][x] > input[y+1][x]):
                        candidate = False
                elif (y == len(input)-1):
                    if (input[y][x] > input[y-1][x]):
                        candidate = False
                else:
                    if ((input[y][x] > input[y-1][x]) or (input[y][x] > input[y+1][x])):
                        candidate = False

            if (candidate):
                kaart.append((x,y))

    print(kaart)
    for (x,y) in kaart:
        result += int(input[y][x])+1


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

