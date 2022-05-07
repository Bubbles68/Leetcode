class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        O(n**2) time and O(1) space solution

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]


        """
        # O(n) time and O(n) space solution
        di = {}
        for index, i in enumerate(nums):
            newtar = target - i
            if newtar in di:
                return (index, nums.index(newtar))
            di[i] = newtar
