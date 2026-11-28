class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target <= i[-1]:
                left = 0
                right = len(i) -1
                while left <= right:
                    mid = (left +right)//2
                    if i[mid] == target:
                        return True
                    elif target > i[mid]:
                        left = mid +1
                        continue
                    else:
                        right = mid -1
                        continue
                return False
        return False