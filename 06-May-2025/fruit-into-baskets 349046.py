# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        trees  = defaultdict(int)
        ans = 0
        left = 0
        n = len(fruits)

        for i in range(n):
            trees[fruits[i]] += 1

            while len(trees) > 2:
                trees[fruits[left]] -= 1
                if  trees[fruits[left]] == 0:
                    del trees[fruits[left]]
                left += 1
                

            ans = max(ans, i - left + 1)

        return ans
            



                