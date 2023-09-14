import sys
import heapq

[n] = [int(x) for x in sys.stdin.readline().split()]

intervals = []

for i in range(n):
    [start, end] = [int(x) for x in sys.stdin.readline().split()]
    # Sort by end time
    heapq.heappush(intervals, (end, start))

schedule = [heapq.heappop(intervals)]

while len(intervals) > 0:
    new = heapq.heappop(intervals)

    # Take the interval if it starts after the last selected interval ends
    if new[1] >= schedule[-1][0]:
        schedule.append(new)

print(len(schedule))
