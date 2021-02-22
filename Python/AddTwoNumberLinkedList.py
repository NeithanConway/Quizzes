# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = ""
        node = self
        while node:
            result += f"{node.val} "
            node = node.next

        return result


class Solution:
    maxNodeValue = 9

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        resultList = ListNode()
        nextNode = resultList
        carry = 0

        while l1 or l2:
            sum = (0 if not l1 else l1.val) + (0 if not l2 else l2.val) + carry
            carry = 1 if sum > self.maxNodeValue else 0
            sum %= 10

            nextNode.val = sum

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

            if l1 or l2:
                nextNode.next = ListNode()
                nextNode = nextNode.next
            elif carry != 0:
                nextNode.next = ListNode(carry)

        return resultList


linkedList1 = ListNode(2)
linkedList1.next = ListNode(4)
linkedList1.next.next = ListNode(3)

linkedList2 = ListNode(5)
linkedList2.next = ListNode(6)
linkedList2.next.next = ListNode(4)

print(Solution().addTwoNumbers(linkedList1, linkedList2))

linkedList1 = ListNode(9)
linkedList1.next = ListNode(9)
linkedList1.next.next = ListNode(9)

linkedList2 = ListNode(9)

print(Solution().addTwoNumbers(linkedList1, linkedList2))