class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize variables to store the current and maximum subarray sums
        current_sum = nums[0]
        max_sum = nums[0]

        # Iterate through the array from left to right
        for num in nums[1:]:
            # Update the current sum by choosing the maximum of the current sum and the current element
            current_sum = max(current_sum + num, num)

            # Update the maximum sum by choosing the maximum of the current sum and the maximum sum
            max_sum = max(current_sum, max_sum)

        # Return the maximum sum
        return max_sum
