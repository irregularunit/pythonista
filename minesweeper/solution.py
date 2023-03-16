def minesweeper(grid):
    rows, cols = len(grid), len(grid[0])
    res = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                res[i][j] = 9
            else:
                count = 0
                for x, y in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                    if 0 <= i + x < rows and 0 <= j + y < cols:
                        count |= grid[i + x][j + y] << ((x + 1) * 3 + y + 1)
                res[i][j] = bin(count).count('1')
    return res
