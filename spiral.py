"""
Given a 2D array, print it spiral from.

Input:
        1    2   3   4
        5    6   7   8
        9   10  11  12
        13  14  15  16
Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
"""

def spiral_form(m, n, a):
    """
    k - starting row index
    m - ending row index
    l - starting column index
    n - ending colum index
    i - iterator
    """
    k = 0
    l = 0

    while (k < m and l < n):
        #Print the first row from the remaining rows
        for i in range(l , n):
            print(a[k][i], end = " ")
        k += 1
        #Print the last column from the remaining colums
        for i in range(k, m):
            print(a[i][n - 1], end= " ")
        n -= 1
        #Print the last row from the remaining rows.
        if (k < m):
            for i in range(n- 1, (1 - 1), -1):
                print(a[m - 1][i], end = " ")
            m -= 1
        #Print the first colum from the remaining columns
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(a[i][l], end = " ")
            l += 1

a = [[1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18]]

R = 3
C = 6
spiral_form(R, C, a)
