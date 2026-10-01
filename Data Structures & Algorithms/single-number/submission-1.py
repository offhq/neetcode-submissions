class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        curr = None
        for num in nums:
            if not curr:
                curr = num
            else:
                curr ^= num
        return curr
            