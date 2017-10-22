#Eigen Vectors of a 2 x 2 matrices
import cmath


def eigenvalue1(a1, a2, b1, b2):
    discriminant = ((b2 + a1) ** 2) - (4 * ((a1 * b2) - (a2 * b1)))
    lambda1 = ((b2 + a1) - cmath.sqrt(discriminant)) / 2
    return lambda1


def eigenvalue2(a1, a2, b1, b2):
    discriminant = ((b2 + a1) ** 2) - (4 * ((a1 * b2) - (a2 * b1)))
    lambda2 = ((b2 + a1) + cmath.sqrt(discriminant)) / 2
    return lambda2


def eigenvector1_of_matrix(l1):
    top = a1 - l1
    bottom = - b1
    eigenvector1 = (top, bottom)
    return eigenvector1


def eigenvector2_of_matrix(l2):
    top = a1 - l2
    bottom = - b1
    eigenvector2 = (top, bottom)
    return eigenvector2


a1 = float(input("Enter value for a1:"))
a2 = float(input("Enter value for a2:"))
b1 = float(input("Enter value for b1:"))
b2 = float(input("Enter value for b2:"))
l1 = eigenvalue1(a1, a1, b1, b2)
l2 = eigenvalue2(a1, a2, b1, b2)
print(l1, l2)
vector1 = eigenvector1_of_matrix(l1)
vector2 = eigenvector2_of_matrix(l2)
print(vector1)
print(vector2)



