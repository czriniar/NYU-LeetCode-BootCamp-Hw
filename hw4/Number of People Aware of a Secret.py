class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7

        # Initialize a dp array to keep track of the number of people who know the secret at each day
        dp = [0] * (n + 1)

        # The first person knows the secret on day 1
        dp[1] = 1

        # Loop through each day starting from day 2
        for day in range(2, n + 1):
            # Calculate the number of people who knew the secret on the previous day
            total_knew_yesterday = dp[day - 1]

            # Calculate the number of people who forget the secret on this day
            people_forget_today = dp[max(day - forget, 0)]

            # Calculate the number of new people who learn the secret on this day
            new_knew_today = total_knew_yesterday - people_forget_today

            # Calculate the number of people who knew the secret delay days ago
            people_knew_delay_ago = dp[max(day - delay, 0)]

            # Update the number of people who know the secret today
            dp[day] = (dp[day - 1] + new_knew_today) % MOD

        return dp[n]
