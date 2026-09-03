class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) == 0:
            return []
        
        #create hasmap of counts
        dict_nums = {}
        for chr in nums:
            dict_nums[chr] = dict_nums.get(chr, 0) + 1
        # print(dict_nums)
        arr = []
        for key in dict_nums.keys():
            array_in = []
            array_in.append(dict_nums[key])
            array_in.append(key)
            arr.append(array_in)

        arr.sort(key = lambda x :x[0], reverse = True)

        result = []

        for ind in range(k):
            result.append(arr[ind][1])

        return result

