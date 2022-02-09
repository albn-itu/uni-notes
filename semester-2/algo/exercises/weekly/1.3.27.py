"""
    Constantly loop throught the linked list until you hit node.next = None
    While looping check if the key is larger than the previous largest
"""

"""
    To delete an element at k, we would assume we are given the first element.
    Then we have to find the element after it and set it to the new next
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(node: Node, data):
    if not node: # If this is the first element
        return Node(data)
    
    tmp = Node(data) # Create a node
    tmp.next = node # Set the new nodes next element to the head
    node = tmp # Set the first element to the new element
    return tmp # Return the new first element

def get_largest(node: Node):
    # THe given node isnt a node
    if node == None:
        return 0
    
    # The given node is the only element
    if node.next == None:
        return node.data

    # The current node must have the largest up intil that point
    # Since its the first
    largest = node.data

    # Loop through the elements
    while(node.next != None):
        # Set the current node reference to the next one
        node = node.next

        # Check if the current nodes data is larger than the number currently registeret
        if node.data > largest:
            # If it is set the new largest
            largest = node.data
    
    # Return it
    return largest

