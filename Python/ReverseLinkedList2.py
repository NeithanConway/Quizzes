# Given the head of a singly linked list and two integers left and
# right where left <= right, reverse the nodes of the list from position
# left to position right, and return the reversed list.


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
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head

        curr_node = head
        prev_node, left_node = None, None
        last_node, right_node = None, None
        counter = 1

        while curr_node and counter <= right:
            if counter < left:
                prev_node = curr_node
            if counter == left:
                left_node = curr_node
            if counter == right:
                right_node = curr_node
                last_node = right_node.next

            curr_node = curr_node.next
            counter += 1

        right_node.next = None

        right_node = self.reverseList(left_node)

        if prev_node:
            prev_node.next = right_node
        else:
            head = right_node

        left_node.next = last_node

        return head

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
list_node.next.next.next.next = ListNode(4)
print(list_node)
print(Solution().reverseBetween(list_node, 2, 4))

list_node = ListNode(0)
print(list_node)
print(Solution().reverseBetween(list_node, 1, 1))

list_node.next = ListNode(1)
print(list_node)
print(Solution().reverseBetween(list_node, 1, 2))