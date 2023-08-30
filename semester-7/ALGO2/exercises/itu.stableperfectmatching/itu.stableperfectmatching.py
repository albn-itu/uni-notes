import sys
from collections import defaultdict

[n, m] = [int(x) for x in sys.stdin.readline().split()]

# Read the graph
graph = defaultdict(list)

for i in range(n):
    names = sys.stdin.readline().split()
    preference_map = defaultdict(int)
    for j in range(1, len(names)):
        preference_map[names[j]] = j

    graph[names[0]] = preference_map

# Find the bipartite graph
color = defaultdict(int)

queue = [names[0]]
color[names[0]] = 1
while queue:
    current = queue.pop(0)

    for v in graph[current]:
        if color[v] == 0:
            color[v] = 1 - color[current]
            queue.append(v)
        # This is wrong if the graph is not bipartite
        # There is validity check

print(color)

proposers = []
rejecters = []
for k, v in color.items():
    if v == 0:
        proposers.append(k)
        graph[k] = list(graph[k].keys())
    else:
        rejecters.append(k)


# Find the stable perfect matching
valid = True

matches = defaultdict(str)
while proposers:
    proposer = proposers.pop(0)
    if len(graph[proposer]) == 0:
        valid = False
        break

    rejecter = graph[proposer].pop(0)

    if rejecter not in matches:
        matches[rejecter] = proposer
        # print(f"{proposer} and {rejecter} are engaged")
    else:
        rejecter_partner = matches[rejecter]
        rejecter_partner_value = graph[rejecter][rejecter_partner]

        proposer_value = graph[rejecter][proposer]

        if proposer_value < rejecter_partner_value:
            matches[rejecter] = proposer
            proposers.append(rejecter_partner)
            # print(f"{proposer} and {rejecter} are engaged")

        else:
            proposers.append(proposer)
            # print(f"{rejecter} rejects {proposer}")

if valid:
    for k, v in matches.items():
        print(f"{k} {v}")
else:
    print("-")
