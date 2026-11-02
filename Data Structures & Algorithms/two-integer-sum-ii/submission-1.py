class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # find 2 indicies that add up to an target 
        # and return them 
        left = 0 
        right = len(numbers) - 1
        returnList = list()

        while(left < right):
            leftVal = numbers[left]
            rightVal = numbers[right]
            sumation = leftVal + rightVal 
            if sumation == target: 
                returnList.append(left + 1)
                returnList.append(right + 1)
                return returnList
            
            elif sumation > target: right -= 1 

            else: left += 1  

        