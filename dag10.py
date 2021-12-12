#!python3
import os
import datetime

# Test input
input = [
"[({(<(())[]>[[{[]{<()<>>",
"[(()[<>])]({[<{<<[]>>(",
"{([(<{}[<>[]}>{[]{[(<()>",
"(((({<>}<{<{<>}{[]{[]{}",
"[[<[([]))<([[{}[[()]]]",
"[{[{({}]{}}([{[{{{}}([]",
"{<[[]]>}<{[{[{[]{()[[[]",
"[<(<(<(<{}))><([]([]()",
"<{([([[(<>()){}]>(<<{{",
"<{([{{}}[<[[[<>{}]]]>[]]"
]

# input integers separated by commas
#input= [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def ismatch(o,c):
    if (c == "(") : return (o == ")")
    if (c == "<") : return (o == ">")
    if (c == "{") : return (o == "}")
    if (c == "[") : return (o == "]")

def solve1():
    result = 0
    openers = {'(':')', '{':'}', "[":"]", "<":">"}
    closers = {')':'(', '}':'{', ']':'[', '>':'<'}
#    openers = ["(", "{", "[", "<"]
    incomplete = []
    for l in input:
        ch = []
        for i in l:
            if i in openers:
                ch.append(i)
            else:
                if not ismatch(i, ch.pop()):
                    if (i == ")"): result += 3
                    if (i == "]"): result += 57
                    if (i == "}"): result += 1197
                    if (i == ">"): result += 25137
                    incomplete.append(l)
                    break

    print("Deel 1: " + str(result))

def solve(line):
    # Look from end to start for openers
    # Look from the opener to a matching closer
    # If found: delete slice
    # If not found: add closer at end and delete slice
    # solve remaining line
    # Protip: reverse the string
    return True

def solve2():


    result = "No"
    print("Deel 2: " + str(result))


start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)


# Stolen solution

score_table = {")": 3, "]": 57, "}": 1197, ">": 25137, "(": 1, "[": 2, "{": 3, "<": 4}
matching_chars = {")": "(", "]": "[", "}": "{", ">": "<"}
open_chars = matching_chars.values()

score_p1 = 0
scores_p2 = []
for line in input:
    stack = []
    for c in line.strip():
        if c in open_chars:
            stack.append(c)
        else:
            if matching_chars[c] == stack[-1]:
                stack.pop()
            else:
                score_p1 += score_table[c]
                break
    else:
        # No break out of the loop, so this line must be incomplete
        score = 0
        while len(stack) > 0:
            c = stack.pop()
            score *= 5
            score += score_table[c]
        scores_p2.append(score)

print(f"Part 1: {score_p1}")

ordered = sorted(scores_p2)
score_p2 = ordered[len(scores_p2) // 2]
print(f"Part 2: {score_p2}"
)

