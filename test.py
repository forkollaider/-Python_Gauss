# coding=utf-8
import numpy

import gauss


a = numpy.array([[3., 2, -5, -1],
                 [2, -1, 3, 13],
                 [1, 2, -1, 9]])
print(a)
print("\n")


b = gauss.gaussFunc(a,gauss.backTrace,gauss.vectorN)
print("Ответ:")
print(b[0])
print("Погрешность:")
print(b[1])
