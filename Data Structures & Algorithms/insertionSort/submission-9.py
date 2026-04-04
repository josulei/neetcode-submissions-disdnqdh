# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        results = []
        lengthPairs = len(pairs)
        for i in range(lengthPairs):
            j = i -1 
            
            while j>=0: 
                if pairs[j].key > pairs[j+1].key:
                    temp = pairs[j+1]
                    pairs[j+1] = pairs[j]
                    pairs[j] = temp
                j-=1
            results.append(pairs[:])
            
        return results