import numpy

import gauss


a = numpy.array([[2., 2, 1, 1],
                 [1, 2, 1, 1],
                 [0, 1, 1, 2]])
print(a)
print("\n")

b = gauss.gaussFunc(a)
print("Ответ:")
print(b)
