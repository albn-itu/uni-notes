from sys import stdout, stdin
from collections import defaultdict

def bfs(graph,src,dest,mincap=0): # returns path to dest
    parent = {src:src}
    layer = [src]
    while layer:
        nextlayer = []
        for u in layer:
            for v,cap in graph[u].items():
                if cap > mincap and v not in parent:
                    parent[v] = u
                    nextlayer.append(v)
                    if v == dest:
                        p =  []
                        current_vertex = dest
                        while src != current_vertex:
                            p.append((parent[current_vertex],current_vertex))
                            current_vertex = parent[current_vertex]
                        return (True,p)
        layer = nextlayer
    return (False,set(parent))
    
def flow(orggraph, src,dest):
    graph = defaultdict(lambda: defaultdict(int))
    maxcapacity = 0
    for u,d in orggraph.items():
        for v,c in d.items():
            graph[u][v] = c
            maxcapacity = max(maxcapacity,c)

    current_flow = 0
    mincap = maxcapacity
    while True:
        ispath,p_or_seen = bfs(graph,src,dest,mincap)
        if not ispath:
            if mincap > 0:
                mincap = mincap // 2
                continue
            else:
                return current_flow
        p = p_or_seen
        saturation = min( graph[u][v] for u,v in p )
        current_flow += saturation
        for u,v in p:
            graph[u][v] -= saturation
            graph[v][u] += saturation

if __name__ == "__main__":
    [n, m, p] = map(int, next(stdin).split())
    graph = defaultdict(lambda: defaultdict(int))

    source = 0
    sink = n + m + p + 2

    uncatted_toys = set()

    for child in range(1, n + 1):    
        graph[source][child] = 1

        toys = list(map(int, next(stdin).split()))[1:]
        for toy in toys:
            toy_id = n + toy
            uncatted_toys.add(toy_id)
            graph[child][toy_id] = 1

    for category in range(1, p + 1):
        cat_id = n + m + category

        cat_toys = list(map(int, next(stdin).split()))[1:]
        amount = cat_toys[-1]
        cat_toys = cat_toys[:-1]

        for toy in cat_toys:
            toy_id = n + toy
            if toy_id in uncatted_toys:
                uncatted_toys.remove(toy_id)

            graph[toy_id][cat_id] = 1

        graph[cat_id][sink] = amount

    for toy in uncatted_toys:
        graph[toy][sink] = 1

    flow = flow(graph, source, sink)

    stdout.write(f"{flow}\n")
