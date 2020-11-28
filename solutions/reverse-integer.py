class Solution:
    def reverse(self, x: int) -> int:
        b = str(x)
        reverse = b[::-1]
        is_negative = True
        # If number is negative, set to false. 
        if reverse.find('-') == -1:
            is_negative = False
        
        reverse = reverse.strip('-')
        
        # make sure it won't overflow
        if int(reverse) > 2147483647:
            return 0
        
        # Loop through entire and remove all starting 0's
        if len(reverse) > 1:
            # if reverse[0] == '0':
            while(reverse[0] is '0'):
                reverse = reverse[1:]
        
        # Add '-' back in if negative
        if is_negative:
            reverse = "{}{}".format('-', reverse)
            
        return reverse
        