# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result, stack = [], []
        curr = root

        while curr or stack:
            if curr:
                result.append(curr.val)
                stack.append(curr)
                curr = curr.right
            else:
                curr = stack.pop()
                curr = curr.left

        result.reverse()
        return result

        # stack = [root]
        # visited = [False]
        # result = []

        # while stack:
        #     curr, v = stack.pop(), visited.pop()
        #     if curr:
        #         if v:
        #             result.append(curr.val)
        #         else:
        #             stack.append(curr)
        #             visited.append(True)
        #             stack.append(curr.right)
        #             visited.append(False)
        #             stack.append(curr.left)
        #             visited.append(False)

        # return result

        # result = []
        # def postorder(root):
        #     if not root:
        #         return
        #     postorder(root.left)
        #     postorder(root.right)
        #     result.append(root.val)

        # postorder(root)
        # return result