class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        arr = []
        candy_counter = 0
        for i in range(0, num_people):
            arr.append(0) 
        while candies > 0:
            for i in range(0, num_people):
                if candy_counter + 1 >= candies:
                    arr[i] += candies
                    return arr
                else:
                    arr[i] += candy_counter + 1
                    candies -= candy_counter + 1
                    candy_counter += 1
        return arr