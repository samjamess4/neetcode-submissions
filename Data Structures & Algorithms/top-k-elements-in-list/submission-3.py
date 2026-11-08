class Solution:
    from collections import defaultdict
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = defaultdict(int) # this mean the vals are gonna be an int 

        for num in nums:
            counts[num] += 1
        
        sortednums = sorted(counts, key = lambda x: counts[x] , reverse = True)

        return sortednums[:k]
        # store all the elments in n dict wiht the number and the count

        # and then sort by the count of values in the dict and then splice the array so its the top k most  


        








        