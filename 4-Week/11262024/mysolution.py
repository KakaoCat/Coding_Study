class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        m = len(matrix)-1
        n = len(matrix[0])-1
        up = 0; down = m; left = 0; right= n; mid1=0; mid2=0

        while up<=down:
            mid1 = (up+down) // 2 
            if matrix[mid1][0] > target:
                down = mid1 - 1
            elif matrix[mid1][n] < target:
                up = mid1 + 1
            
            else: 
                while left<=right:
                    mid2 = (left + right) // 2
                    if matrix[mid1][mid2] == target:
                        return True
                    elif matrix[mid1][mid2] < target:
                        left = mid2 +1
                    else:
                        right = mid2 -1
                break

        return False
