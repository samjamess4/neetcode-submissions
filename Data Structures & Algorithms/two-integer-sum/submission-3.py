class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # taret is an int 

        #in my opinion this is easiest with an 2 pointer technique 

        seen = dict()
        returnList = list()


        for i in range(len(nums)): 
            sumValue = target - nums[i]

            if sumValue in seen.keys():
                # 
                
                returnList.append(seen[sumValue])
                returnList.append(i)
                return returnList
            else: 
                seen[nums[i]] = i


                

        