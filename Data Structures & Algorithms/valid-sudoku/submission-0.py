class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}

        cols = {}

        squares = {}

        for r in range(9):

            for c in range(9):

                num = board[r][c]

                # Ignore empty cells

                if num == ".":

                    continue

                # Identify the 3x3 box

                box = (r // 3, c // 3)

                # Create sets if they don't exist

                if r not in rows:

                    rows[r] = set()

                if c not in cols:

                    cols[c] = set()

                if box not in squares:

                    squares[box] = set()

                # Check for duplicates

                if num in rows[r]:

                    return False

                if num in cols[c]:

                    return False

                if num in squares[box]:

                    return False

                # Store the number

                rows[r].add(num)

                cols[c].add(num)

                squares[box].add(num)

        return True