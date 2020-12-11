class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        final1 = []
        for char in S:
            if char == "#":
                final1 = final1[:-1]
            else:
                final1.append(char)
        final2 = []
        for char in T:
            if char == "#":
                final2 = final2[:-1]
            else:
                final2.append(char)
        return final1 == final2