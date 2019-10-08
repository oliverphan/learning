# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []
        
        curr = head
        while curr != None:
            stack.append(curr)
            curr = curr.next
            
        # At this point all items in list should be in the stack.
        
        # Start the new list with last item.
        if len(stack) > 0:
            rev_list = stack.pop()

            curr = rev_list
            # Keep popping items and adding to new list
            while len(stack) > 0:
                curr.next = stack.pop()
                curr = curr.next
			
			# Make sure last element isn't a cycle.
            curr.next = None
        else:
            rev_list = None
            
        return rev_list
		

	def iterativeReverse(self, head: ListNode) -> ListNode:
		prev = None
		curr = head
		
		while curr != None:
			nextTemp = curr.next
			curr.next = prev
			prev = curr
			curr = nextTemp
			
		return prev
		
	def recursiveReverse(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head;
        
        # Gives you a reversed list except for head
        p = self.reverseList(head.next)
        
        # Set second node to point 'next' to head
        head.next.next = head
        
        # Then head should point to none
        head.next = None
        return p