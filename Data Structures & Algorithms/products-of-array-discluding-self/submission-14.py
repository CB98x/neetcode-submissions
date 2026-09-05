class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #count 0, all non-zero items multiple
        m = 1
        count_0 = 0
        for i in nums:
            if i != 0:
                m = m * i
            else:
                count_0 += 1
        print(m)
        
        result = []

        #case 1: One Zero
        if count_0 == 1:
            for i in nums:
                if i == 0:
                    result.append(m)
                else: 
                    result.append(0)
            return result

        #case 2: Two Zeros
        if count_0 > 1:
            for i in nums:
                result.append(0)
        
        #Case 3: No zeros - divide nums[i] for each position
        if count_0 == 0:
            for i in range(len(nums)):
                if nums[i] == 0:
                    result.append(m)
                else: 
                    result.append(round(m/nums[i]))

        return result
        