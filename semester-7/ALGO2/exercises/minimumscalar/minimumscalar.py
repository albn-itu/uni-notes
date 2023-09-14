import sys

for case in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    x = sorted(list(map(int, sys.stdin.readline().split())))
    y = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

    s = 0
    for i in range(n):
        s += x[i] * y[i]

    print("Case #{}: {}".format(case + 1, s))
