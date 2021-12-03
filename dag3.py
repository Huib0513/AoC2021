#!python3
import os
import datetime
import re

# Test input
input = ["00100", "11110", "10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]

# input integers separated by commas
#input= [int(i) for i in open("input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def filter(input, position, filtervalue):
    return([i for i in input if i[position] == filtervalue])

def solve1():
    solution = []
    for t in range(len(input[0])):
        solution.append("1" if (sum(int(i[t]) for i in input) > len(input)/2) else "0")
    gamma = int("".join(solution),2)
    epsilon = int("".join(solution),2)^(pow(2,len(input[0]))-1)
    print("Deel 1: " + str(gamma)+" * "+ str(epsilon) + " = " + str(gamma*epsilon))

def solve2():
    oxygen = co2 = input
    for t in range(len(oxygen[0])):
        #print("oxygen = " + str(oxygen))
        fv = "1" if (sum(int(i[t]) for i in oxygen) >= len(oxygen)/2) else "0"
        oxygen = filter(oxygen, t, fv)
        if (len(oxygen) == 1): break
    for t in range(len(co2[0])):
        #print("co2 = " + str(co2))
        fv = "1" if (sum(int(i[t]) for i in co2) < len(co2)/2) else "0"
        co2 = filter(co2, t, fv)
        if (len(co2) == 1): break 

    print(str(oxygen), str(co2))
    print("Deel 2: " + str(int("".join(oxygen),2)*int("".join(co2),2)))



start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
