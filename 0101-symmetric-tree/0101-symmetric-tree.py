# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        
        queue = deque()
        # 루트의 왼쪽과 오른쪽을 큐에 넣음
        queue.append((root.left, root.right))
        
        while queue:
            t1, t2 = queue.popleft()
            
            # 둘 다 없으면 다음으로 넘어감
            if not t1 and not t2:
                continue
            # 하나만 없거나 값이 다르면 대칭 아님
            if not t1 or not t2 or t1.val != t2.val:
                return False
            
            # 대칭되는 노드끼리 큐에 넣기
            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))
        
        return True