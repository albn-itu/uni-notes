pairs = []
n=0

pizzas = []
subset = []

def search(k):
    if k == n+1:
        pizzas.append(subset[:])
    else:
        valid = True
        for i in range(0, len(pairs)):
            (j, l) = pairs[i]

            if (k == j and l in subset) or (k == l and j in subset):
                valid = False
                break
                
        search(k+1)
        if valid:
            subset.append(k)
            search(k+1)
            subset.pop()

(n,m) = map(int, input().split())
for i in range(0, m):
    (j, l) = map(int, input().split())
    pairs.append((j,l))

search(1)
print(len(pizzas))
