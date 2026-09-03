class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # build dict 1
        d1 = {}
        for char in s:
            d1[char] = d1.get(char, 0) + 1
        # build dict 2
        d2 = {}
        for char in t:
            d2[char] = d2.get(char, 0) + 1
        # compare?
        if d1 == d2:
            return True
        else:
            return False