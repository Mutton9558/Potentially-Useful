class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Traverse both linked lists
        while l1 or l2 or carry:
            # Get values from l1 and l2, defaulting to 0 if the list is finished
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and the carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to the next nodes in the lists
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy_head.next

l1 = Solution()
l1.append(2)
l1.append(4)
l1.append(3)
l2 = Solution()
l2.append(5)
l2.append(6)
l2.append(4)

solution = Solution()
result = solution.addTwoNumbers(l1.head, l2.head)

# Function to print the resulting linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

# Print the result
print_linked_list(result)
