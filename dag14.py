#!python3
import os
import datetime
from collections import Counter
from collections import defaultdict

# Test input
input = [
"NNCB",
"",
"CH -> B",
"HH -> N",
"CB -> H",
"NH -> C",
"HB -> C",
"HC -> B",
"HN -> C",
"NN -> C",
"BH -> H",
"NC -> B",
"NB -> B",
"BN -> B",
"BB -> N",
"BC -> B",
"CC -> N",
"CN -> C"]

# input integers separated by commas
#input= [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
#input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def step(start:list):
    result = ""
    for l in range(1,len(start)):
        result += start[l-1] + insertions[start[l-1]+start[l]]

    return result + start[len(start)-1]

def step2(start:defaultdict):
    result = defaultdict(int)
    for k in start.keys():
        bla = k[0] + insertions[k]
        bloe = insertions[k] + k[1]
        result[bla] += start[k]
        result[bloe] += start[k]

    return result


def solve1():
    polymer = template
    for i in range(10):
        polymer = step(polymer)
        teller = Counter(polymer)
        print(i, teller)

    print(teller.most_common()[0], teller.most_common()[:-2:-1][0])
    result = int(teller.most_common()[0][1]) - int(teller.most_common()[:-2:-1][0][1])
    print("Deel 1: " + str(result))


def solve2():
    combilist = {template[i-1:i+1]:1 for i in range(1,len(template))}
    for i in range(40):
        combilist = step2(combilist)
        if i == 9:
            teller = Counter()
            for k in combilist.keys():
                teller[k[0]] += combilist[k]
                #teller[k[1]] += combilist[k]
            teller[template[-1]] += 1
            #teller[template[0]] -= 1
            high = teller.most_common()[0][1] #/2
            low = teller.most_common()[:-2:-1][0][1] #/2
            print(high, low)
            result = high - low
            print("Deel 1: " + str(result))

    teller = Counter()
    for k in combilist.keys():
        teller[k[0]] += combilist[k]
        #teller[k[1]] += combilist[k]
    teller[template[-1]] += 1
    #teller[template[0]] -= 1
    high = teller.most_common()[0][1] #/2
    low = teller.most_common()[:-2:-1][0][1] #/2
    print(high, low)
    result = high - low
    print("Deel 2: " + str(result))

template = input[0]
insertions = {f[0]:f[1] for f in [l.split(" -> ") for l in input[2:]]}

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
