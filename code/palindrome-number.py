class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If less than 0, it will have a "-" char
        if x < 0:
            return False
        # Convert x into a string
        b = str(x)
        # Reverse the string and store as z
        z = b[::-1]
        # If they are equal, return true
        if b == z:
            return True
        else:
            return False