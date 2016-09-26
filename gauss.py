# coding=utf-8

from sys import float_info as fi
from numpy import array,zeros,where
from copy import deepcopy

def gaussFunc(modifiedMatrix, backTraverseCallBack, residualCallback):

    modifiedMatrix = array(modifiedMatrix)
    inputMatrixCopy = array(modifiedMatrix)
    matrixRowCount = len(modifiedMatrix)
    matrixColumnCount = matrixRowCount + 1

    for index,row in enumerate(modifiedMatrix):
        max_value = max(modifiedMatrix.T[index], key=lambda x: abs(x))
        if abs(max_value) < fi.epsilon:
            raise DeterminatorException("Check Determinant")

        factor = float(modifiedMatrix[index][index])
        modifiedMatrix[index] = map(lambda x: x / factor, modifiedMatrix[index])
        subsractRowIndex = index + 1

        for sri in xrange(subsractRowIndex,matrixRowCount):
            downstairNumber = modifiedMatrix[sri][index]
            for i in xrange(index,matrixColumnCount):
                modifiedMatrix[sri][i]  = modifiedMatrix[sri][i] - modifiedMatrix[index][i] * downstairNumber

    result = [backTraverseCallBack(modifiedMatrix, matrixRowCount), None]


    return result



class DeterminatorException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def backTrace(a, len1):  # обратный ход
    a = array(a)
    i = len1 - 1
    while i > 0:
        j = i - 1
        while j >= 0:
            a[j][len1] = a[j][len1] - a[j][i] * a[i][len1]
            j -= 1
        i -= 1
    return a[:, len1]


def vectorN(c, a, len1):  # c-начальная матрица a-ответ len1-кол столбцов, vectB-вектор B
    c = array(c)
    a = array(a)
    vectB = deepcopy(c[:, len1])
    b = zeros((len1))
    i = 0

    while i < len1:  # подставляем полученные x-ы, в матрицу, получаем вектор невязки
        j = 0
        while j < len1:
            b[i] += c[i][j] * a[j]
            j += 1
        i = i + 1

    c = deepcopy(b)
    print("!")

    for i in range(len1):
        c[i] = abs(c[i] - vectB[i])  # отнимаем от вектора невязки вектор B
        # получаем норму
    return c
