class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        for char in s:
            map1[char] = s.count(char)
        for char in t:
            map2[char] = t.count(char)
        return map1 == map2