import sys

string = list(sys.stdin.readline())

toDelete = 0
for i in range(len(string)-1, -1, -1):
    if string[i] == "<":
        toDelete += 1
        string[i] = ""
    elif toDelete > 0:
        string[i] = ""
        toDelete -= 1

print("".join(string))
