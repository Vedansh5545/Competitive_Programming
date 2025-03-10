def generate_spiral_matrix(n: int):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    left, right = 0, n - 1
    top, bottom = 0, n - 1

    while left <= right and top <= bottom:

        # Traverse from Left to Right
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Traverse Downward
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Traverse from Right to Left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        # Traverse from Bottom to Top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix



print(generate_spiral_matrix(3))