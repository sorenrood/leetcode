class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        word1_instances = []
        word2_instances = []
        
        for i in range(0, len(words)):
            if words[i] == word1:
                word1_instances.append(i)
            if words[i] == word2:
                word2_instances.append(i)
        
        min_dif = 99999
        
        for i in word1_instances:
            for j in word2_instances:
                if abs(i - j) < min_dif:
                    min_dif = abs(i - j)
        return min_dif