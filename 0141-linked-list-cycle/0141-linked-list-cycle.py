# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next         # 한 칸 이동
            fast = fast.next.next    # 두 칸 이동

            if slow == fast:
                return True          # 두 포인터가 만나면 사이클 존재

        return False 