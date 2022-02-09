"""
    To remove the last item of the linked list one would have to loop through to find the second to last item.
    Once found set that elements next to None
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

def removeLast(node: Node):
    # THe given node isnt a node
    if node == None:
        return None
    
    # The given node is the last element
    if node.next == None:
        node = None
        return None

    # Since the above then the best case scenario is that this is the second to last element
    second_to_last = node

    # Find the second to last element
    while(second_to_last.next.next):
        second_to_last = second_to_last.next
    
    # Set the second to last elements next element to None
    # By doing this we remove the last element from the list
    second_to_last.next = None
    return node

