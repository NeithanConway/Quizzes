# Given the head of a singly linked list, reverse the list, and return the reversed list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        res = str(self.val)
        if self.next:
            res += str(self.next)
        return res


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev_node = None
        while head:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node

        return prev_node


list_node = ListNode(0)
list_node.next = ListNode(1)
list_node.next.next = ListNode(2)
list_node.next.next.next = ListNode(3)
print(list_node)
print(Solution().reverseList(list_node))
