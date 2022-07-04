class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        # record order of ascending from left & r.
        ls, rs = [1] * n, [1] * n
        for i in range(1, n):
            if ratings[i] - ratings[i - 1] > 0:
                ls[i] = ls[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] - ratings[i + 1] > 0:
                rs[i] = rs[i + 1] + 1
        return sum([max(ls[i], rs[i]) for i in range(n)])