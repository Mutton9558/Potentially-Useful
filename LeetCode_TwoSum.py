class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = []
        for i, num in enumerate(nums):
            complement = target - num
            if complement in index_map:
                result = [index_map.index(complement), i]
                break
            index_map.append(num)
            
        return result
