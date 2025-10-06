class Solution(object):
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        if k == 1:
            return nums
        
        result = [0] * (n - k + 1)
        # Manual deque using list
        dq = [0] * n  # pre-allocate
        front, rear = 0, -1
        
        for i in range(n):
            # Remove out-of-window from front
            if front <= rear and dq[front] <= i - k:
                front += 1
            
            # Maintain decreasing order from rear
            while front <= rear and nums[dq[rear]] <= nums[i]:
                rear -= 1
            
            rear += 1
            dq[rear] = i
            
            # Add to result
            if i >= k - 1:
                result[i - k + 1] = nums[dq[front]]
        
        return result
