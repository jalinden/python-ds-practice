def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2], 0,0 1,1
        ...     [30, 40], 0,1 1,0
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3], 0,0 1,1 2,2 
        ...    [4, 5, 6], 0,2 1,1 2,0
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    n = len(matrix)
    sum_first_diagonal = sum(matrix[i][i] for i in range(n))
    sum_second_diagonal = sum(matrix[i][n-i-1] for i in range(n))
    total = sum_first_diagonal + sum_second_diagonal
    return total

