def minesweeper(grid):
    rows, cols = len(grid), len(grid[0])
    res = [[0] * cols for _ in range(rows)]

    bit_positions = [
        ((row + 1) * 3 + col + 1, row, col)
        for row, col in [
            (i, j)
            for i in range(-1, 2)
            for j in range(-1, 2)
            if i or j 
        ]
    ]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                res[i][j] = 9
            else:
                count = 0
                for bit, x, y in bit_positions:
                    ni, nj = i + x, j + y
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj]:
                        count |= 1 << bit
                res[i][j] = count.bit_count()
    return res


if __name__ == "__main__":
    import time

    def time_func(func, in_):
        start = time.perf_counter()
        out = func(in_)
        end = time.perf_counter()

        time_taken = end - start
        return time_taken, out

    final_1 = [[1, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 1, 1],
            [1, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 1],
    ]

    solution = [[9, 9, 2, 0, 0, 0, 0, 0], [9, 9, 2, 0, 0, 1, 1, 1], [4, 4, 2, 0, 0, 1, 9, 1], [9, 9, 2, 2, 3, 4, 3, 2], [3, 3, 3, 9, 9, 9, 9, 3], [2, 9, 2, 3, 4, 5, 9, 9], [9, 3, 2, 3, 9, 4, 4, 4], [1, 2, 9, 3, 9, 3, 9, 9]]

    t1 = 0
    for _ in range(1000):
        s1, is_correct = time_func(minesweeper, final_1)
        t1 += s1
        if not is_correct == solution:
            print("Incorrect")
            break

    print("minesweeper: ", t1)
