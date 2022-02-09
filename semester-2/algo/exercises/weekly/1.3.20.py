"""
    To delete an element at k, we would assume we are given the first element.
    Then we have to find the element after it and set it to the new next
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def push(node: Node, data):
    if not node:  # If this is the first element
        return Node(data)

    tmp = Node(data)  # Create a node
    tmp.next = node  # Set the new nodes next element to the head
    node = tmp  # Set the first element to the new element
    return tmp  # Return the new first element


def delete(node: Node, k: int):
    # THe given node isnt a node
    if node == None:
        return None

    # The given node is the last element
    if node.next == None:
        node = None
        return None

    # Find the element at k
    element_before = node
    element = node
    for i in range(0, k):
        # The linked list isnt that long
        if element.next == None:
            return None

        element_before = element
        element = element.next

    # If the element we found is the last element of the list
    if element.next == None:
        element = None
        element_before.next = None
    else:
        # Set the element befores next to the element after the element we want to delete
        element_before.next = element.next
        element = None
