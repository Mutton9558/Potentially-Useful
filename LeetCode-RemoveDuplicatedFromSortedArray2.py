# Essentially you have an array and you wish to remove duplicates from said array such that you can have at most 2 of the same elements on the array for example [0,0,1,1]
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        i = 0
        while i < length:
            j = i
            repetition = 0
            while j < length-1:
                if nums[j] == nums[j+1]:
                  # gets the amount of duplicates for one element
                    repetition+=1
                    j+=1
                else:
                    break
            if i < length - 1:  # Ensure i+1 is within bounds
                # ensures that it only removes elements whereby there exist more than 2 in the array
                if nums[i] == nums[i+1] and repetition >=2:
                    nums.pop(i+1)
                    length -= 1
                else:
                    i += 1
            else:
                i+=1
