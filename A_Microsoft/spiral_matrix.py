class Solution:
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []

        row_start, col_start = 0, 0
        row_end, col_end = len(matrix), len(matrix[0])
        res = []

        while row_start <= row_end - 1 and col_start <= col_end - 1:
            for x in range(col_start, col_end):
                res.append(matrix[row_start][x])
            row_start += 1

            for x in range(row_start, row_end):
                res.append(matrix[x][col_end - 1])
            col_end -= 1

            if row_start <= row_end - 1:
                for x in range(col_end - 1, col_start - 1, -1):
                    res.append(matrix[row_end - 1][x])
                row_end -= 1

            if col_start <= col_end - 1:
                for x in range(row_end - 1, row_start - 1, -1):
                    res.append(matrix[x][col_start])
                col_start += 1

        return res
