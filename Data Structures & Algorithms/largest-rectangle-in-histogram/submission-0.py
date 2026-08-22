class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        next_smaller_to_left = [-1] * n
        next_smaller_to_right = [n] * n
        stack = []
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                next_smaller_to_left[i] = stack[-1]
            stack.append(i)

        stack.clear()

        for i in range(n-1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                next_smaller_to_right[i] = stack[-1]
            stack.append(i)
        max_area = 0
        for i in range(n):
            width = next_smaller_to_right[i] - next_smaller_to_left[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)
        return max_area
