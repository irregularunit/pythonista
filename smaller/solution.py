def smaller(arr):
    n = len(arr)
    c, i = [0] * n,list(range(n))

    def merge(indices):
        if len(indices) > 1:
            mid = len(indices) // 2
            left = indices[:mid]
            right = indices[mid:]

            merge(left)
            merge(right)

            i, j = 0, 0
            while i < len(left) and j < len(right):
                if arr[left[i]] <= arr[right[j]]:
                    c[left[i]] += j
                    indices[i+j] = left[i]
                    i += 1
                else:
                    indices[i+j] = right[j]
                    j += 1

            while i < len(left):
                c[left[i]] += j
                indices[i+j] = left[i]
                i += 1

            while j < len(right):
                indices[i+j] = right[j]
                j += 1

    merge(i)
    return c


if __name__ == "__main__":
    x = [5, 4, 3, 2, 1]
    y = [1, 2, 0]

    tests = [
        (x, [4, 3, 2, 1, 0]),
        (y, [1, 1,0]),
    ]
    for arr, expected in tests:
        assert smaller(arr) == expected
