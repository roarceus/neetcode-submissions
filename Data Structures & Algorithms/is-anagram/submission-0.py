class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        h1, h2 = {}, {}

        for letter in s:
            if letter in h1:
                h1[letter] += 1
            else:
                h1[letter] = 1

        for letter in t:
            if letter in h2:
                h2[letter] += 1
            else:
                h2[letter] = 1

        return h1 == h2
