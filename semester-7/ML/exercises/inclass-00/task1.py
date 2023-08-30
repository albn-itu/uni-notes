from math import sqrt

a = [180, 70, 10, 0, 4]
b = [165, 55, 8, 1, 7]
c = [175, 60, 9, 0, 3]

task11 = 0
for i in range(0, len(a)):
    task11 += (a[i]-b[i])**2

task11 = sqrt(task11)
print(f"Task 1.1: {task11}")


aminb = []
for i in range(0, len(a)):
    aminb.append(a[i]-b[i])

task12 = 0
for i in range(0, len(aminb)):
    task12 += aminb[i]**2

task12 = sqrt(task12)

print(f"Task 1.2: {task12}")

print("Task 1.3: In code the process is essentially the same, but if one where to do the calculations by hand the second method is much easier to manually reason about")


def euclidian_distance(a, b):
    dist = 0
    for i in range(0, len(a)):
        dist += (a[i]-b[i])**2

    return sqrt(dist)


ab_dist = euclidian_distance(a, b)
ac_dist = euclidian_distance(a, c)
bc_dist = euclidian_distance(b, c)

print(f"Task 1.4: {ab_dist}, {ac_dist}, {bc_dist}")
if ab_dist < ac_dist and ab_dist < bc_dist:
    print("Task 1.4: a and b are the closest")
elif ac_dist < ab_dist and ac_dist < bc_dist:
    print("Task 1.4: a and c are the closest")
else:
    print("Task 1.4: b and c are the closest")
