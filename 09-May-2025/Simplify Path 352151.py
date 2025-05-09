# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path_list = path.split('/')
        res = []

        for char in path_list:

            if char == "." or char ==  "":
                continue
                res.append(char)

            elif char == ".." :
                if res:
                    res.pop(-1)

            else:
                res.append(char)
                

            print(path_list)
        
        return "/" + ('/').join(res)