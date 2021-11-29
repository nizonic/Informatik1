#!/usr/bin/env python3
# The signatures of this class and its public methods are required for the automated grading to work.
# You must not change the names or the list of parameters.
# You may introduce private/protected utility methods though.
class Matrix:

    def __init__(self, matrix):
        for i in range(len(matrix) -1):
            if matrix[i] < matrix[i+1]:
                raise AssertionError
        if matrix == [[]]:
            raise AssertionError
        if not matrix:
            raise AssertionError
        def getDepth(matrix):
            try:
                len(matrix)
                return getDepth(matrix[0]) + 1
            except:
                return 0

        if getDepth(matrix) > 2:
            raise AssertionError


        self.__matrix = matrix
        # Implement this function and perform required checks
        # create adequate instance variables and check whether they should be private or public


    # To implement the required functionality, you will also have to implement two more
    # of the special functions that include a double underscore as per the task description.



    # DO NOT CHANGE the functions below! Consider also implementing __repr__ and __str__ for nice printing


    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        else:
            return self.__matrix == other.__matrix

    def __hash__(self):
        return hash(tuple([tuple(row) for row in self.__matrix]))

    def __add__(self, other):
        A = self.__matrix
        B = other.__matrix
        result = [map(sum, zip(*t)) for t in zip(A, B)]
        return result

    def __mul__(self, other):
        A = self.__matrix
        B = other.__matrix
        c = []
        for i in range(0, len(A)):
            temp = []
            for j in range(0, len(B[0])):
                s = 0
                for k in range(0, len(A[0])):
                    s += A[i][k] * B[k][j]
                temp.append(s)
            c.append(temp)
        return c

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
    T = Matrix([[5,5],[5,5], [2,3]])
    print(M)
    print(M == T)
    d = {M: "1", T: "2"}
    d.update({M: "3"})
    print(d)
    C = M * T
    print(C)
