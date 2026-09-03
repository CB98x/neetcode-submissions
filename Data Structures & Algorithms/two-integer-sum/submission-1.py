class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #for each item in list, calc complement and find location in dict of all, where i != j
        #create dict
        dict = {}
        for ind in range(len(nums)):
            dict[nums[ind]] = ind
        #check complement ind in dict
        for ind in range(len(nums)):
            comp = target -  nums[ind]
            if comp in dict.keys():
                if ind != dict[comp]:
                    return [ind, dict[comp]] 
