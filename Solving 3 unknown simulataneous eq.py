#Solving simulataneous equations with 3 unknowns


def three_x_three():
    print("Type in first equation in format below")
    a1 = int(input("X coefficient:"))
    b1 = int(input("Y Coefficient:"))
    c1 = int(input("Z Coefficient:"))
    ans1 = int(input("Answer:"))
    print("Now the second equation")
    a2 = int(input("X coefficient:"))
    b2 = int(input("Y Coefficient:"))
    c2 = int(input("Z Coefficient:"))
    ans2 = int(input("Answer:"))
    print("Now for the third equation")
    a3 = int(input("X Coefficient:"))
    b3 = int(input("Y Coefficient:"))
    c3 = int(input("Z Coefficient:"))
    ans3 = int(input("Answer:"))
    det1 = (b2 * c3) - (b3 * c2)
    det2 = (a2 * c3) - (a3 * c2)
    det3 = (a2 * b3) - (a3 * b2)
    det = (a1 * det1) - (b1 * det2) + (c1 * det3)
    cofactorA1 = (b2 * c3) - (b3 * c2)
    cofactorA2 = -((b1 * c3) - (b3 * c1))
    cofactorA3 = (b1 * c2) - (b2 * c1)
    cofactorB1 = -((a2 * c3) - (a3 * c2))
    cofactorB2 = (a1 * c3) - (a3 * c1)
    cofactorB3 = -((a1 * c2) - (a2 * c1))
    cofactorC1 = (a2 * b3) - (a3 * b2)
    cofactorC2 = -((a1 * b3) - (a3 * b1))
    cofactorC3 = (a1 * b2) - (a2 * b1)
    x = 1/det * (cofactorA1 * ans1 + cofactorA2 * ans2 + cofactorA3 * ans3)
    y = 1/det * (cofactorB1 * ans1 + cofactorB2 * ans2 + cofactorB3 * ans3)
    z = 1/det * (cofactorC1 * ans1 + cofactorC2 * ans2 + cofactorC3 * ans3)
    print("x =", x, "y =", y, "z =", z)
three_x_three()





