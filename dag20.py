#!python3
import os
import datetime
from collections import Counter
from collections import defaultdict

# Test input
input = [
"..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#",
"",
"#..#.",
"#....",
"##..#",
"..#..",
"..###"]

# input integers separated by commas
#input= [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

algo = input[0]
image = {}
minx = miny = 0
maxx = len(input[2])
maxy = len(input)-2
for y, l in [(y,l) for y,l in enumerate(input[2:])]:
    for i in range(len(l)):
        if l[i] == "#": image[y,i] = 1 

def checkcell(start:dict, row:int, col:int, parity: int) -> int:
    index = ""
    for y in range(row-1,row+2):
        for x in range(col-1,col+2):
            if ((y,x) in start.keys()):
                index += "1"
            elif  (
                (not ((minx < x < maxx) and (miny < y < maxy)))
                 and (parity % 2)):
                index += "1"
            else:
                index += "0"
    return int(index,2)

def step(start:dict, nr:int) -> dict:
    global minx, maxx, miny, maxy
    result = {}
    for row in range(miny-1, maxy+2):
        for col in range(minx-1, maxx+2):
            index = checkcell(start, row, col, nr)
            if (algo[index] == "#"):
                result[row, col] = 1
                if col > maxx: maxx = col
                if col < minx: minx = col
                if row > maxy: maxy = row
                if row < miny: miny = row
            elif ((row, col) in result): result.pop((x,y))

    return result

def photoprinter(photo:dict):
    for row in range(minx, maxx+1):
        regel = ""
        for col in range(miny, maxy+1):
            regel += "#" if (row, col) in photo.keys() else "."
        print(regel)
    print("".join(["-" for x in range(minx, maxx+1)]))

def solve1():
    sharper = step(image, 1)
    sharpest = step(sharper, 2)
    photoprinter(sharper)
    photoprinter(sharpest)
    result = len(sharpest)
    print("Deel 1: " + str(result))


def solve2():
    result = "No"
    print("Deel 2: " + str(result))


photoprinter(image)
start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
