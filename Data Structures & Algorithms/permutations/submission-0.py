class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        in_cur = set()
        def dfs():
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            for num in nums:
                if num not in in_cur:
                    cur.append(num)
                    in_cur.add(num)

                    dfs()

                    cur.pop()
                    in_cur.remove(num)
        dfs()
        return res


            

                

        