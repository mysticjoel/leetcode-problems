class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # If range is too small to have two primes
        if right - left < 1 or right < 2:
            return [-1, -1]
        
        # Create sieve up to right
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False
        
        # Mark non-primes in sieve
        for i in range(2, int(right ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, right + 1, i):
                    sieve[j] = False
        
        # Find primes in range [left, right]
        primes = []
        for i in range(max(2, left), right + 1):
            if sieve[i]:
                primes.append(i)
        
        # If less than 2 primes found
        if len(primes) < 2:
            return [-1, -1]
        
        # Find minimum gap
        min_gap = float('inf')
        result = [-1, -1]
        
        for i in range(len(primes) - 1):
            gap = primes[i + 1] - primes[i]
            if gap < min_gap:
                min_gap = gap
                result = [primes[i], primes[i + 1]]
        
        return result
