# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        result = []

        while q:
            qLen = len(q)
            level = None
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level = node.val
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level)

        return result