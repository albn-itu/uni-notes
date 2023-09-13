import math
import random
import sys


class Point:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __str__(self):
        return f"{self.x} {self.y}"

    def __repr__(self):
        return f"{self.x} {self.y}"

    def sub(self, other):
        return Point([self.x - other.x, self.y - other.y])


def cmp_list(point, points):
    min_dist = float("inf")
    min_point = None

    for other_point in points:
        if other_point is point:
            continue
        dist = point.distance(other_point)
        if dist < min_dist:
            min_dist = dist
            min_point = other_point

    return min_dist, min_point


def estimate_b(points):
    rand_point = random.choice(points)
    min_dist, min_point = cmp_list(rand_point, points)

    return min_dist, [rand_point, min_point]


def get_diff(delta):
    return delta / 3


def determine_subsquare(point, delta):
    diff = get_diff(delta)

    return math.floor(point.x / diff), math.floor(point.y / diff)


def make_grid(points, delta):
    grid = {}

    for point in points:
        subsquare = determine_subsquare(point, delta)
        if subsquare not in grid:
            grid[subsquare] = []
        grid[subsquare].append(point)

    return grid


def nearest_squares(point, grid, delta):
    square = determine_subsquare(point, delta)
    x = square[0]
    y = square[1]

    neighbors = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            sq = (x + i, y + j)
            if sq in grid:
                neighbors += grid[sq]

    return neighbors


def algo(points):
    min_delta, min_delta_points = estimate_b(points)
    delta = min_delta
    if delta == 0:
        return delta, min_delta_points

    grid = make_grid(points, delta)

    for i in range(len(points)):
        point = points[i]
        squares = nearest_squares(point, grid, delta)
        new_min_delta, new_min_delta_point = cmp_list(point, squares)

        if new_min_delta < min_delta:
            min_delta = new_min_delta
            min_delta_points = [point, new_min_delta_point]

        if min_delta == 0:
            return min_delta, min_delta_points

    return min_delta, min_delta_points


def main():
    n = int(sys.stdin.readline())

    points = []
    for _ in range(n):
        points.append(Point([float(x) for x in sys.stdin.readline().split()]))

    delta, answer = algo(points)
    for point in answer:
        print(point)


if __name__ == "__main__":
    main()
