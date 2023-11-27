#!python3
import os
import datetime

# Test input
input = [
"be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
"edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
"fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
"fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
"aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
"fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
"dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
"bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
"egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
"gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
]

# input integers separated by commas
#input= [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
#input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()


def solve1():
    result = 0
    things = [c.split() for c in [i.split(" | ")[1] for i  in input]]
    for t in things:
        for e in t:
            l = len(e)
            if ((l==2) or (l==3) or (l==4) or (l==7)):
                result +=1
    print("Deel 1: " + str(result))

def solve2():
    display = [c.split() for c in [i.split(" | ")[1] for i  in input]]
    inputlines = [c.split() for c in [i.split(" | ")[0] for i  in input]]
    #print(inputlines)
    for counter in range(len(inputlines)):
        l=inputlines[counter]
        code = {}
        code[1] = [i for i in l if len(i) == 2][0]
        code[7] = [i for i in l if len(i) == 3][0]
        code[4] = [i for i in l if len(i) == 4][0]
        code[8] = [i for i in l if len(i) == 7][0]
        for i in [i for i in l if len(i) == 6]:
            if len(i) == 6:
                if ((i.find(code[1][0]) != -1) and 
                    (i.find(code[1][1]) != -1)): # Contains 1
                    code[0] = i
                else:
                    code[6] = i
        for i in [i for i in l if len(i) == 5]:
            if len(i) == 5:
                if ((i.find(code[1][0]) != -1) and (i.find(code[1][1]) != -1)): # Contains 1
                    code[3] = i
                elif (len(set(i).intersection(set(code[6]))) == 5):
                    code[5] = i
                else:
                    code[2] = i

        lineresult = ""
        d = display[counter]
        for v in d:
            for i in range(0,9):
                if (set(code[i]) == set(v)) :
                    lineresult += str(i)
                    break
        print(lineresult)
    #print(code)


    
    #while True:
        #for l in inputs:

    result = "No"
    print("Deel 2: " + str(result))


start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)

