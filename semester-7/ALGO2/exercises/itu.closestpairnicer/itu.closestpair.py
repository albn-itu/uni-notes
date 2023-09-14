import sys
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __init__(self, point):
        self.x = point[0]
        self.y = point[1]

    def dist(self, b):
        return math.sqrt((self.x - b.x)**2 + (self.y - b.y)**2)

    def __str__(self):
        return f"{self.x:.2f} {self.y:.2f}"

    def __repr__(self):
        return self.__str__()


def strip_points(points, mid, delta):
    stripped = []
    for i in range(len(points)):
        if abs(points[i].x - mid.x) < delta:
            stripped.append(points[i])

    return stripped


def brute_force(points, n):
    delta = float('inf')
    closest = []

    for i in range(n):
        for j in range(i+1, n):
            dist = points[i].dist(points[j])
            if dist <= delta:
                delta = dist
                closest = [points[i], points[j]]

    return closest, delta


def strip_closest_pair(points, closest, delta):
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if (points[j].y - points[i].y) < delta:
                break

            dist = points[i].dist(points[j])

            if dist < delta:
                delta = dist
                closest = [points[i], points[j]]

    return closest, delta


def min_res(a, b):
    a_points, a_delta = a
    b_points, b_delta = b

    if a_delta <= b_delta:
        return a
    else:
        return b


def closest_pair(points_x, points_y, n):
    if n <= 3:
        return brute_force(points_x, n)

    mid = n//2
    mid_point = points_x[mid]

    left_points = []
    right_points = []
    for point in points_y:
        if point.x <= mid_point.x and len(left_points) < mid:
            left_points.append(point)
        else:
            right_points.append(point)

    left_res = closest_pair(points_x[:mid], left_points, mid)
    right_res = closest_pair(points_x[mid:], right_points, n-mid)

    closest, delta = min_res(left_res, right_res)

    stripped_points = strip_points(points_y, mid_point, delta)
    closest, delta = min_res((closest, delta), strip_closest_pair(
        stripped_points, closest, delta))

    return closest, delta


def main():
    n = int(sys.stdin.readline())

    points_x = []
    points_y = []

    for i in range(n):
        point = Point([float(x) for x in sys.stdin.readline().split()])
        points_x.append(point)
        points_y.append(point)

    points_x.sort(key=lambda x: x.x)
    points_y.sort(key=lambda x: x.y)

    points, delta = closest_pair(points_x, points_y, n)

    for point in points:
        print(point)


if __name__ == '__main__':
    main()
