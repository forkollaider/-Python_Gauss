import gauss
import numpy

a = numpy.array([[1., 2, 1, 1],
                [1, 2 , 1, 1],
                [0, 1, 1, 2]])
#a= numpy.array([[ 1. ,  0.6, -0.4,  0.4],
               # [ 0.,   1.,  -1.5,  1.5],
               # [ 0.,   0.,   1.,   1. ]])
print(a)
print("\n")

b = gauss.gaussFunc(a)
print("Ответ:")
print(b)
