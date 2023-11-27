#!python3
import os
import datetime
from collections import Counter
from collections import defaultdict

# Test input
#Player 1 starting position: 6
#Player 2 starting position: 1

# input integers separated by commas
#input= [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
#input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()


def solve1():
    throw = score1 = score2 = 0
    start = 1
    pos1 = 6 - 1
    pos2 = 1 - 1
    while ((score1 < 1000) and (score2 < 1000)):
        throw += 3
        pos1 = (pos1 + ((3 * start) + 3)) % 10
        score1 += pos1 + 1
        start += 3
        if (throw < 30):
            print(throw, pos1+1, score1, pos2+1, score2)
        if (score1 < 1000):
            throw += 3
            pos2 = (pos2 + ((3 * start) + 3)) % 10
            score2 += pos2 + 1
            start += 3
        if (throw < 30):
            print(throw, pos1+1, score1, pos2+1, score2)

    print(throw, score1, score2)
    result = throw * min(score1, score2)
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
