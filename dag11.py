#!python3
import os
import datetime

# Test input
input = [
"5483143223",
"2745854711",
"5264556173",
"6141336146",
"6357385478",
"4167524645",
"2176841721",
"6882881134",
"4846848554",
"5283751526"
]

# input integers separated by commas
#input= [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def get_neighbours(yin:int, xin:int, maxy:int, maxx:int):
    for y in [yin-1, yin, yin+1]:
        for x in [xin-1, xin, xin+1]:
            if (((y>=0) and (y<=maxy)) and
               ((x >= 0) and (x <= maxx)) and
               not ((x == xin) and (y == yin))):
                yield y,x


def solve1():
    kaart = [[int(x) for x in r] for r in input]
    result = 0
    step = 0

    while True:
        step += 1
        flashed = []
        #print(step, kaart)
        for r in range(len(kaart)):
            for c in range(len(kaart[r])):
                kaart[r][c] += 1

        # Check for flashes
        flashdetector = True
        while flashdetector:
            flashdetector = False
            for r in range(len(kaart)):
                for c in range(len(kaart[r])):
                    if (kaart[r][c] >= 10):
                        kaart[r][c] = 0
                        flashed.append((r,c))
                        flashdetector = True
                        for y,x in get_neighbours(r,c,len(kaart)-1, len(kaart[r])-1):
                            if not (y,x) in flashed:
                                kaart[y][x] += 1

        result += len(flashed)

        if (step == 100):
            print("Deel 1: " + str(result))
        if (not (sum([sum(x) for x in kaart]))):
            print("Deel 2: "+ str(step))
            break

def solve2():


    result = "No"
    print("Deel 2: " + str(result))


start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
