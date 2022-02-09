"""
    insertAfter()
    Check if the next element is the last
    If it is then set new element as the next, a normal push operation.
    If it isnt, then save the reference to the new element in a variable newNode and do:
    newNode.next = node.next
    node.next = newNode
"""