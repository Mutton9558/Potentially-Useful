class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        nums[:] = nums[-k:] + nums[:-k]
        print(nums)

test = Solution()
nums = [#enter a list of elements]
test.rotate(nums, k #k is the number of rotations)
  
