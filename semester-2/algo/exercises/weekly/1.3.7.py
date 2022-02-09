"""
    If we assume that a theoretical Stack class uses a linked list.
    Then it would insert a new item as the first_item. And whenever a new item is added the pointer is moved down, aka first_item.next = oldFirst.
    Then by definition our first_item would be the top element, and to pop it we would return the first_item, and say first_item = first_item.next.
    Thereby to peek we would only have to say return first_item
"""