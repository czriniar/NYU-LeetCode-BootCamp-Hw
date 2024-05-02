class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Calculate the total sum of the array
        total_sum = sum(nums)

        # Check if the total sum is even
        if total_sum % 2 != 0:
            return False

        # Set the target sum to half of the total sum
        target_sum = total_sum // 2

        # Initialize a memo to store the results of subproblems
        memo = [False] * (target_sum + 1)

        # Set the base case: if the remaining sum is 0, return True
        memo[0] = True

        # Iterate through the array from left to right
        for num in nums:
            # Iterate through the memo from right to left
            for i in range(target_sum, num - 1, -1):
                # Try including the current element
                memo[i] = memo[i] or memo[i - num]

        # Return the result of the last subproblem
        return memo[target_sum]
