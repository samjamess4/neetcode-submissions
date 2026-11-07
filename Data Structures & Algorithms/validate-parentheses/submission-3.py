class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {"(": ")", "{": "}", "[": "]"}
        stacky = [] # stacks in python are lists 
        if len(s) == 1:
            return False

        for char in s:
            if char in "({[":
                stacky.append(char)
            else: 
                if not stacky or pairs[stacky.pop()] != char:
                    return False

        
        

            
        return not stacky

            




        