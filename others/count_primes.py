from math import sqrt


class Solution:
    def is_prime(self, n: int) -> bool:
        m = int(sqrt(n))
        for i in range(2, m):
            if n % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        c = 0
        for j in range(n):
            if self.is_prime(j):
                c += 1
        return c


class SolutionSieveofEratosthenes:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        m = int(sqrt(n)) + 1
        for i in range(2, m):
            if not primes[i]:
                continue
            # primes[i*i:n:i] = [False] * len(primes[i*i:n:i])
            for j in range(i*i, n, i):
                primes[j] = False
        return sum(primes)
