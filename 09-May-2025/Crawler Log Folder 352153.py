# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = []

        for action in logs:
            if action == "../":
                if res:
                    res.pop()
            elif action == "./":
                continue
            else:
                res.append(action)
            
        return len(res)