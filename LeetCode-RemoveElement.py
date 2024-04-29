# not proud of this one
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num = len(nums)
        i = 0
        while i<num:
            if nums[i] == val:
                nums.pop(i)
                num-=1  
                if i>0:
                    i-=1
            else:
                i+=1
