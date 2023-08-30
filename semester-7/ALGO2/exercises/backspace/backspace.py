import sys

string = sys.stdin.readline()
out = ""

toDelete = 0
lastDelete = 0
for i, c in enumerate(string):
    if c == "<":
        toDelete += 2
    else:
        if toDelete > 0:
            out = string[lastDelete:i - toDelete]
            lastDelete = i
            toDelete = 0
out += string[lastDelete:]
print(out)
