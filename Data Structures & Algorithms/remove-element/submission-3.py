class Solution:
    def removeElement(self, nums: List[int], val: int) -> int: 
        idx = 0
        for curr_val in nums:
            if curr_val != val:
                nums[idx] = curr_val
                idx += 1
        return idx

