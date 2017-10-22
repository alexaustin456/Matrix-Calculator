#Solving 2 unknown simultaneous equations by matrix method


def two_x_two():
    eq1x = int(input("X coefficient:"))
    eq1y = int(input("Y Coefficient:"))
    ans1 = int(input("Answer:"))
    eq2x = int(input("X coefficient:"))
    eq2y = int(input("Y Coefficient:"))
    ans2 = int(input("Answer:"))
    det = (eq1x * eq2y) - (eq1y * eq2x)
    a1 = 1/det*(eq2y)
    b1 = 1/det*(-(eq1y))
    a2 = 1/det*(-(eq2x))
    b2 = 1/det*(eq1x)
    x = (a1 * ans1) + (b1 * ans2)
    y = (a2 * ans1) + (b2 * ans2)
    print("x =", x, "y =", y)
two_x_two()
