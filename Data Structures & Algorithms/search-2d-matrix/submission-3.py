class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Step 1: Find the correct row
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == matrix[mid][-1]:
                return True

            elif target > matrix[mid][-1]:
                left = mid + 1

            else:
                right = mid - 1

        if left == len(matrix):
            return False

        i = matrix[left]

        # Step 2: Search within the row
        left = 0
        right = len(i) - 1

        while left <= right:
            mid = (left + right) // 2

            if i[mid] == target:
                return True

            elif target > i[mid]:
                left = mid + 1

            else:
                right = mid - 1

        return False