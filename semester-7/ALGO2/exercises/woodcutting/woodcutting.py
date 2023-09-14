import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    customers = []

    for _ in range(n):
        customers.append(sum(list(map(int, sys.stdin.readline().split()))[1:]))

    customers.sort()

    s = 0
    ans = 0
    for c in customers:
        s += c
        ans += s / n

    print(ans)
