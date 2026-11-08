class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        res = []
        prefix = 1 
        # putting prefix inside the loop re-declares prefix eveytime 




        for i in range(len(nums)):
            

            prefixresult = prefix * nums[i]
            res.append(prefix)
            prefix = prefixresult
        
        postfix = 1 
        
        for j in range(len(nums ) - 1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]

        return res
            



        