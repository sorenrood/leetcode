class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        check = list(A[0])
        for word in A[1:]:
            new_check = []
            for c in word:
                if c in check:
                    new_check.append(c)
                    check.remove(c)
            check = new_check
        return check