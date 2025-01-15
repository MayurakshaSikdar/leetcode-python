# 2130. Maximum Twin Sum of a Linked List


# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.
# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

# Example 1:
# Input: head = [5,4,2,1]
# Output: 6
# Explanation:
# Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
# There are no other nodes with twins in the linked list.
# Thus, the maximum twin sum of the linked list is 6. 

# Example 2:
# Input: head = [4,2,2,3]
# Output: 7
# Explanation:
# The nodes with twins present in this linked list are:
# - Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
# - Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
# Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 

# Example 3:
# Input: head = [1,100000]
# Output: 100001
# Explanation:
# There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.

# Constraints:
# The number of nodes in the list is an even integer in the range [2, 10^5].
# 1 <= Node.val <= 10^5


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        n = 0
        temp = head
        values = []
        while temp:
            n += 1
            values.append(temp.val)
            temp = temp.next
        max_sum = -1
        i, j = 0, n-1
        while i < j:
            if max_sum < (values[i] + values[j]):
                max_sum = values[i] + values[j]
            i += 1
            j -= 1
        return max_sum










# Function to create a linked list from a list of values
def create_linked_list(values):
    if not values:  # Handle empty list case
        return None
    
    head = ListNode(values[0])  # Create the head node
    current = head
    
    for value in values[1:]:
        current.next = ListNode(value)  # Create the next node
        current = current.next  # Move to the next node
    
    return head

# Values for the linked list
values = [4, 2, 2, 3]

# Create the linked list
head = create_linked_list(values)

# Function to print the linked list (for testing)
def print_linked_list(head):
    current = head
    temp = []
    while current:
        temp.append(str(current.val))
        current = current.next
    return ' -> '.join(temp)


# Print the linked list
print(print_linked_list(head))

val = Solution().pairSum(head)

print(val)