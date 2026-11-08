class Solution:

    from collections import defaultdict 

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # return sublist of words that are anagrams 
        # we can use an set and check for specific string and lens i think 
        anaset = set()
        subarrays = []
        sort = sorted(strs)

        groups = defaultdict(list)

        for st in strs:
           sortst =  "".join(sorted(st))
           groups[sortst].append(st)

            # you want the key to be the sorted string 
            #and the value stored to be the original val. 
        return list(groups.values())



       