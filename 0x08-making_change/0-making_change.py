#!/usr/bin/python3
"""
contains the makeChange funct
the feweest
"""


def makeChange(coins, total):
    """
    fewest number of coins needed to meet the given total.

    Args:
        coins (list): A list of the value
        total (int): amount to reach.

    Returns:
        int: number of coinsreach the total,
             or -1 not possible.
    """
    if total <= 0:
        return 0

    # the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins are needed to make 0

    # Loop through d each sub-totthe minimum
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still inf
    return dp[total] if dp[total] != float('inf') else -1
