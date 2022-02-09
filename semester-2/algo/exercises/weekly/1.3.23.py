t = 0
t.next = 1
x = 2
x.next = 3

x.next = t # x.next = 0
t.next = x.next # t.next = 0

# Equivalent
t = 0
t.next = 0
x.next = 0
x = 3

# The code doesnt do the same as we overwrite x.next before we overwrite t.next
# This means that t.next actually gets the value of t. So t, t.next and x.next are all t
# The previous code inserted t after x, while this inserts t after x, and then inserts t after t