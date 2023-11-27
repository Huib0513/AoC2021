#!python3
import os
import datetime
from collections import Counter

# Test input
input = ["D2FE28"]
#input = ["38006F45291200"] # Operator
#input= ["EE00D40C823060"] # Operator

# input integers separated by commas
#input= [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
#input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

# input single line
#input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read()

def parsepacket(packet): # returns version, ID, list of subpackets
    version = int(packet[0:3],2)
    ID = int(packet[3:6],2)
    if (ID == 4):
        getliteral(packet[6:])
    else:
        if packet[6] == '1': # 11 bits number of subpackets
            subcount = int(packet[7:17],2)
            subpackets = ""
        else: # 15 bits length in bits of subpackets
            sublength = int(packet[7:21],2)
            subpackets = ""

    return version, ID, subpackets

def getliteral(packet):
    index = 6
    group = packet[index:index+5]
    value = ""
    while group[0] == "1":
        value += group[1:]
        index += 5
        group = packet[index:index+5]
    value += group[1:]
    subpackets = [int(value,2)]


def solve1():
    version, ID, subs = parsepacket(binput)
    result = "No"
    print("Deel 1: " + str(result))


def solve2():
    result = "No"
    print("Deel 2: " + str(result))

mapper = {
"0":"0000",
"1":"0001",
"2":"0010",
"3":"0011",
"4":"0100",
"5":"0101",
"6":"0110",
"7":"0111",
"8":"1000",
"9":"1001",
"A":"1010",
"B":"1011",
"C":"1100",
"D":"1101",
"E":"1110",
"F":"1111"
}

binput = "".join([mapper[l] for l in input[0]])
print(binput)

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
