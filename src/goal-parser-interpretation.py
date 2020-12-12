class Solution:
    def interpret(self, command: str) -> str:
        final = ''
        i = 0
        
        while i < len(command):
            if command[i] == 'G':
                final += 'G'
                i += 1
            
            elif command[i] == '(':
                if command[i + 1] == ')':
                    final += 'o'
                    i += 2
                    if i >= len(command):
                        return final
                
                elif command[i + 1] == 'a':
                    final += 'al'
                    i += 4
                    if i >= len(command):
                        return final
        return final