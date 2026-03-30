class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif char == ")":
                if self.isEmpty(stack) or stack[-1] != "(":
                    return False
                stack.pop()
            elif char == "}":
                if self.isEmpty(stack) or stack[-1] != "{":
                    return False
                stack.pop()
            elif char == "]":
                if self.isEmpty(stack) or stack[-1] != "[":
                    return False
                stack.pop()

        return self.isEmpty(stack)

    def isEmpty(self, stack):
        return len(stack) == 0