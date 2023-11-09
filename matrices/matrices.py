def mat_mul(A, B):
    row = len(A)
    column = len(B[0])
    # making the matrix based on i * j
    C = [[0 for x in range(column)] for y in range(row)]


    # Base Case
    if len(A[0]) != len(B):
        print("Invalid Dimension")
        return None
    else:
        for i in range(len(A)):
            for j in range(len(B[0])):
                val = 0
                for k in range(len(B)):
                    val += A[i][k] * B[k][j]
                C[i][j] = val

        return C
    


A = [[1, 2],
     [3, 4],
     [5, 6]
    ]

B = [[7],
     [8]]


print(mat_mul(A, B))

# matrix multiplication is also called dot product if the matrices columns are treated a vectors.
