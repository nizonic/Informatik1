#!/usr/bin/env python3
# The signatures of this class and its public methods are required for the automated grading to work.
# You must not change the names or the list of parameters.
# You may introduce private/protected utility methods though.
class Matrix:

    def __init__(self, matrix):
        assert matrix != [], 'empty list'
        assert isinstance(matrix, list), 'not a nested list'
        for row in matrix:
            assert isinstance(row, list), 'not a nested list'
            assert row != [], 'empty sublist'
            assert len(row) == len(matrix[0]), 'matrix not rectangular'
            for num in row:
                assert isinstance(num, (int, float)), 'invalid type in sublist'
        self.__matrix = matrix

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        else:
            return self.__matrix == other.__matrix

    def __hash__(self):
        return hash(tuple([tuple(row) for row in self.__matrix]))

    def __add__(self, other):
        assert isinstance(other, Matrix), "not a matrix"
        A = self.__matrix
        B = other.__matrix
        assert len(A) == len(B), "rows not equal"
        assert len(A[0]) == len(B[0]), "columns not equal"
        result = []
        for i in range(len(A)):
            result.append([])
            for j in range(len(A[0])):
                result[i].append(0)

            # fill in result
        for i in range(len(A)):
            for j in range(len(A[0])):
                result[i][j] = self.__matrix[i][j] + other.__matrix[i][j]
        return Matrix(result)

    def __mul__(self, other):
        assert isinstance(other, Matrix), "not a matrix"
        A = self.__matrix
        B = other.__matrix
        assert len(A[0]) == len(B), "1st matrix columns and 2nd matrix rows don't match up"
        prod = []
        for i in range(len(A)):
            prod.append([])
            for j in range(len(B[0])):
                prod[i].append(0)

        # fill in prods
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    prod[i][j] += self.__matrix[i][k] * other.__matrix[k][j]
        return Matrix(prod)

    def __repr__(self):
        s = ""
        for line in self.__matrix:
            s += str(line)
            if line != self.__matrix[-1]:
                s += "\n"
        return s



# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    M = Matrix([[5,5],[5,5]])
    T = Matrix([[5,5,3],[5,5,3]])
    print(M)
    print(M == T)
    d = {M: "1", T: "2"}
    d.update({M: "3"})
    print(d)
    C = M * T
    print(C)
