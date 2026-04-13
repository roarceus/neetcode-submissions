class Solution:
    def countSubstrings(self, s: str) -> int:
        # 2 Pointers
        # result = 0

        # for i in range(len(s)):
        #     # odd length string
        #     l, r = i, i
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         result += 1
        #         l -= 1
        #         r += 1
            
        #     # even length string
        #     l, r = i, i + 1
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         result += 1
        #         l -= 1
        #         r += 1
            
        # return result

        # 2 Pointers (Optimized)
        result = 0

        for i in range(len(s)):
            result += self.countPalindrome(s, i, i)
            result += self.countPalindrome(s, i, i + 1)
        return result

    def countPalindrome(self, s, l, r):
        result = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1
        return result