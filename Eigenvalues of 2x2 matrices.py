#Method for finding eigenvalues of 2x2 matrix
import cmath


def two_x_two_eigen_values():
    a1 = float(input("Enter value for a1:"))
    a2 = float(input("Enter value for a2:"))
    b1 = float(input("Enter value for b1:"))
    b2 = float(input("Enter value for b2:"))
    discriminant = ((b2 + a1) ** 2) - (4 * ((a1 * b2) - (a2 * b1)))
    lamda1 = ((b2 + a1) - cmath.sqrt(discriminant)) / 2
    lamda2 = ((b2 + a1) + cmath.sqrt(discriminant)) / 2
    print("First eigenvalue =", lamda1, "Second eigenvalue =", lamda2)
two_x_two_eigen_values()
