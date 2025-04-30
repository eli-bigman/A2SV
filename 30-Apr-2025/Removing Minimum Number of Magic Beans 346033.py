# Problem: Removing Minimum Number of Magic Beans - https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)
        prefix_sum = []
        res = []
        acc = 0

        for i in range(n):
            acc += beans[i]
            prefix_sum.append(acc)
        print(prefix_sum)

        total = max(prefix_sum)
        for j in range(n):
            res.append(total - (beans[j] *(n - j)))
        print(res)

        return min(res)