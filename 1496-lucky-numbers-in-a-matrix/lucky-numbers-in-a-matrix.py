class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        lucky_numbers = []
        
        for i in range(m):
            min_row = min(matrix[i])
            min_row_idx = matrix[i].index(min_row)
            
            max_col = max([row[min_row_idx] for row in matrix])
            
            if min_row == max_col:
                lucky_numbers.append(min_row)
        
        return lucky_numbers