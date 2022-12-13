import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import linalg
from mpl_toolkits.mplot3d import Axes3D


def mult_matrix_by_vector(matr, vect):
    res = np.zeros((4, 3))

    res[:, 0] = matr.dot(vect[:, 0])
    res[:, 1] = matr.dot(vect[:, 0])
    res[:, 2] = matr.dot(vect[:, 0])
    return res


def fixed_boundary_condition(n, hord):
    P1_dash = np.array([1.0, 1.0, 1.0])
    Pn_dash = np.array([1.0, 1.0, 1.0])

    M = np.zeros(shape=(n, n))
    M[0, 0] = 1
    M[0, 1] = 0
    M[n - 1, n - 2] = 0
    M[n - 1, n - 1] = 1
    for i in range(1, n-1):
        M[i, i - 1] = hord[i]
        M[i, i] = 2*(hord[i]+hord[i-1])
        M[i, i + 1] = hord[i-1]

    R = np.zeros((n, 3))
    R[0] = P1_dash
    R[n-1] = Pn_dash

    for i in range(1, n-1):

        R[i] = ((P[i - 1] - P[i - 2]) * (hord[i] ** 2) + (P[i] - P[i - 1]) * (hord[i - 1] ** 2)) * (
                    3 / (hord[i - 1] * hord[i]))
    print(M)
    Mt = linalg.inv(M)
    p_dash = mult_matrix_by_vector(Mt, R)
    return p_dash


def weak_boundary_condition(n, hord):
    M = np.zeros(shape=(n, n))
    M[0, 0] = 1
    M[0, 1] = 0.5
    M[n - 1, n - 2] = 2
    M[n - 1, n - 1] = 4

    for i in range(1, n - 1):
        M[i, i - 1] = hord[i]
        M[i, i] = 2*(hord[i]+hord[i-1])
        M[i, i + 1] = hord[i-1]

    R = np.zeros((n, 3))
    R[0] = (P[1] - P[0]) * (3.0 / (2 * hord[0]))
    R[n - 1] = (P[n-1] - P[n - 2]) * (6 / hord[n - 2])

    for i in range(1, n-1):
        R[i] = ((P[i-1]-P[i-2])*(hord[i]**2)+(P[i]-P[i-1])*(hord[i-1]**2))*(3/(hord[i-1]*hord[i]))
    print(M)
    Mt = np.linalg.pinv(M)
    p_dash = mult_matrix_by_vector(Mt, R)
    return p_dash


def build_cubic_spline(P, condition):
    n = P.shape[0]

    hord = []
    for i in range(1, n):
        tk = np.sqrt((P[i][0] - P[i - 1][0]) ** 2 +
                      (P[i][1] - P[i - 1][1]) ** 2 +
                      (P[i][2] - P[i - 1][2]) ** 2)
        hord.append(tk)

    p_dash = condition(n, hord)
    b = np.zeros((n, 4, 3))
    for i in range(n - 1):
        b[i][0] = P[i]
        b[i][1] = p_dash[i]
        b[i][2] = ((P[i + 1] - P[i]) * 3) * (1 / hord[i] ** 2) - (p_dash[i] * 2) * (1 / hord[i]) - p_dash[i + 1] * (
                    1 / hord[i])
        b[i][3] = ((P[i] - P[i + 1]) * 2) * (1 / hord[i] ** 3) + (p_dash[i]) * (1 / hord[i] ** 2) + p_dash[i + 1] * (
                    1 / (hord[i] ** 2))

    x = []
    y = []
    z = []
    for i in range(n - 1):
        for t in np.arange(0, hord[i], 0.01):
            a = b[i][0] + b[i][1] * t + b[i][2] * t ** 2 + b[i][3] * t ** 3
            x.append(a[0])
            y.append(a[1])
            z.append(a[2])
    return np.array(x), np.array(y), np.array(z)


if __name__ == '__main__':
   P = np.array([[1, 1, 1], [1, 2, 1], [2, 1, 2], [2, 2, 2]])

   fig = plt.figure()
   ax = fig.add_subplot(1, 1, 1, projection='3d')
   ax.scatter(P[:, 0], P[:, 1], P[:, 2], color="#FF4500")
   print("M weak condition")
   x1, y1, z1 = build_cubic_spline(P, weak_boundary_condition)
   print("M fixed condition")
   x2, y2, z2 = build_cubic_spline(P, fixed_boundary_condition)

   ax.plot(x1, y1, z1, linewidth=3, color='#3CB371')
   ax.plot(x2, y2, z2, linewidth=1, color='#130000')

   ax.legend(["Кубічний сплайн з слабкими граничними умовами", 'Кубічний сплайн з фіксованими граничними умовами'])
   plt.show()
