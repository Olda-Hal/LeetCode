from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        maxlenght = 0
        for i in range(len(nums)):
            current_lenght = 0
            biggest_num = None
            
            if len(nums) == 1:
                return 1

            if len(nums[i:]) <= maxlenght:
                return maxlenght

            for j in nums[i:]:
                if biggest_num == None:
                    biggest_num = nums[i]
                    current_lenght +=1
                    continue
                if j > biggest_num and j < biggest_num+k:
                    biggest_num = j
                    current_lenght +=1
            if current_lenght > maxlenght:
                maxlenght = current_lenght
                
        

print(Solution().lengthOfLIS([4,2,1,4,3,4,5,8,15], 3)) # 5
print(Solution().lengthOfLIS([7,4,5,1,8,12,4,7], 5)) # 4
print(Solution().lengthOfLIS([1,5], 1)) # 1