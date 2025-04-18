# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = "".join(map(str, digits))
        print(res)

        res = int(res) + 1

        print(res)

        return [int(i) for i in str(res)]