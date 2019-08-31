# T: O(m + n)
# S: O(1)

def searchInSortedMatrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1
    while row <= len(matrix) - 1 and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [row, col]
        
    return [-1, -1]
