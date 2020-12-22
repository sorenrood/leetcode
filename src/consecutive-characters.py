class Solution:
    def maxPower(self, s: str) -> int:
        maximum = 0
        in_row = 0
        last = None
        for char in s:
            if char == last:
                in_row += 1
                if in_row > maximum:
                    maximum = in_row
            if char != last:
                in_row = 1
                last = char
        if maximum == 0:
            return 1
        return maximum