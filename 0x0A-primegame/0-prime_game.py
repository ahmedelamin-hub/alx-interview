#!/usr/bin/python3
def isWinner(x, nums):
    """Determines the winner of the prime number game."""
    
    if not nums or x < 1:
        return None

    # To store prime status of numbers up to the largest number in nums
    max_num = max(nums)
    primes = [True for _ in range(max_num + 1)]
    primes[0], primes[1] = False, False  # 0 and 1 are not prime

    # Implementing the Sieve of Eratosthenes to mark prime numbers
    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    # Counts for wins of Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Loop through each round
    for n in nums:
        prime_count = sum(primes[2:n + 1])

        # If the count of primes is odd, Maria wins (she goes first)
        # If it's even, Ben wins
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the winner based on the number of wins
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
