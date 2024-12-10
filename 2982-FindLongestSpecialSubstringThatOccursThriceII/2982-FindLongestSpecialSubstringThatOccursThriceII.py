class Solution:
    def maximumLength(self, s: str) -> int:
        '''
        Hashmap + heap

        Count streaks of each character.
        Maintain the three longest streaks of each character.
        The maximum of the minimum of the three longest streaks of any character is the result.

        w = size of alphabet
        n = length of s
        k = occurrences to be special
        Time: O(w + n log k)
            - For each element in s (O(n))
                - Push the streak of the previous character to the min heap of longest lengths
                    of special substrings of that character. O(log k)
                - Pop the min heap if its length exceeds 3. O(log k)
                - Update the streak and last character.

            - For each distinct character (O(w)), check the top of the min heap of lengths (O(1)). O(w) * O(1) == O(w)
        Space: O(w * k)
            - Each distinct character maps to a min heap of at most size 3.
        '''
        counts = defaultdict(list)
        streak = 0
        last = ''
        # Use chain with a sentinel to force the last character's streak to be processed.
        for c in itertools.chain(s, ['']):
            # If there are less than three streaks, add the current streak (substring length)
            # to the min heap
            if len(counts[last]) < 3:
                heapq.heappush(counts[last], streak)
            # If there are three streaks, push the current streak and pop the smallest.
            else:
                heapq.heappushpop(counts[last], streak)
            streak = (streak + 1) if c == last else 1
            last = c
        
        return max((streaks[0] for streaks in counts.values() if len(streaks) == 3), default=-1)