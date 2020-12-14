class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        t1 = []
        t2 = []
        for item in word1:
            for char in item:
                t1.append(char)        
        for item in word2:
            for char in item:
                t2.append(char)      
        return t1 == t2