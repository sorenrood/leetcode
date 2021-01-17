class Solution:
    def reformatNumber(self, number: str) -> str:
        
        # preprocessing, take out whitespace and dash symbol
        number = number.replace(' ', '')
        number = number.replace('-', '')
        
        # storage for numbers
        blocks = []
        
        # keep making number blocks of length 3 until remaining length is smaller than 4
        while len(number) > 4:
            
            blocks.append( number[:3])
            number = number[3:]
        
        
        # tail block handling, followed the rule defined in description
        if len(number) <= 3:
            blocks.append( number )
        else:
            blocks.append( number[:2])
            blocks.append( number[2:])
        
		# generate reformatted numbers, separated by dash
        return '-'.join(blocks)  