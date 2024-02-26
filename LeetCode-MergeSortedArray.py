# again just represents the function not full code
# meant to be integrated within code not to exist as a file of it's own
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        n = len(nums2)
        m = len(nums1) - n
        temp = nums1[:m]
        array = temp + nums2
        for i in range(0, len(nums1)):    
            nums1[i] = array[i]
        nums1.sort()
