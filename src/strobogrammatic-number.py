class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        key = {0: 0, 1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 9, 7: 0, 8: 8, 9: 6}
        new = ''
        for x in num: 
            new += str(key[int(x)])
        return new[::-1] == num