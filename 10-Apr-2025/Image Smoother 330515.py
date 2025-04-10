# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        res = [[0]* cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                total = 0
                count = 0

                for x in range(max(0,i-1),min(rows, i+2)):
                    for y in range(max(0,j-1) , min(cols,j+2)):
                        total+=img[x][y]
                        count+= 1

                res[i][j] = total//count
            
        return res
            



