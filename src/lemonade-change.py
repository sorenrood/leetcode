class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for num in bills:
            if num == 5:
                five += 1
            elif num == 10 and five >= 1:
                five -= 1
                ten += 1
            elif num == 20 and five >= 1 and ten >= 1:
                ten -= 1
                five -= 1
            elif num == 20 and five >= 3:
                five -= 3
            else:
                return False
        return True