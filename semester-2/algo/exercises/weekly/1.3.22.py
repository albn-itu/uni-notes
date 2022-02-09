t = 0
t.next = 1
x.next = 2
x = 3

t.next = x.next # t.next = 2
x.next = t # x.next = 0

# Equivalent
t = 0
t.next = 2
x.next = 0
x = 3

# The code then inserts the node t right after x