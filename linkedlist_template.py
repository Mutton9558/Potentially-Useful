# Initialize a node
class Node:
    def __init__(self, data=None) -> None:
        self.data = data # default data is None unless a value is specified
        self.next = None # The last node should have a pointer to NULL

class LinkedList:
    def __init__(self) -> None:
        self.head = Node() # initialize head (start of linked list)

    def append(self, data) -> None:
        new_node = Node(data) # creates new node
        currentData = self.head  
        while currentData.next != None: # iterate through the linked list until it reaches the last node
            currentData = currentData.next
        currentData.next = new_node # declares the next node at the end
    
    def get_length(self) -> int:
        size = 0 # incrementer
        currentData = self.head
        while currentData.next != None:
            size += 1 # Add size as long as the next node is not null
            currentData = currentData.next

        return size

    def display(self):
        arr = []
        currentData = self.head
        while currentData.next != None:
            currentData = currentData.next
            arr.append(currentData.data) # appends the next node's data (this is because we start with an empty node that is head)
        print(arr)

    def erase(self, index):
        if index >= self.get_length():
            print("Out of range")
            return
        else:
            cur_index = 0
            cur = self.head
            while True:
                last_node = cur # saves the previous node
                cur = cur.next # moves the current node up by 1
                if cur_index == index:
                    last_node.next = cur.next # replaces pointer from the previous node to the next node skipping the current node
                    return
                cur_index += 1

# I LOVE POINTERS
