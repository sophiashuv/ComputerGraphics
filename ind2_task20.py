from mpl_toolkits.mplot3d import axes3d, Axes3D
import matplotlib.pyplot as plt
import numpy as np


def F(t):
    T = np.array([t**3, t**2, t, 1])
    M = np.array([[2, -2, 1, 1],
                  [-3, 3, -2, -1],
                  [0, 0, 1, 0],
                  [1, 1, 0, 0]])

    res = np.matmul(M, T)
    return res


def par_to_dec(u_w):
    u, w = u_w
    x = u * (1 - w)
    y = w
    z = u
    return x, y, z


def dec_to_par(x, y, z):
    u = z
    w = y
    return np.array([u, w])


def P01(u, w):
    return np.array([u, 1])


def P10(u, w):
    return np.array([1, w])


def P11(u, w):
    return np.array([1, 1])


def Q(u, w):
    x = np.matmul(np.matmul(P[:, :, 0], F(u)), F(w))
    y = np.matmul(np.matmul(P[:, :, 1], F(u)), F(w))
    z = np.matmul(np.matmul(P[:, :, 2], F(u)), F(w))

    return np.array([x, y, z])


def find_points(u, w):
    points = []
    for uu in u:
        for ww in w:
            points.append(Q(uu, ww))
    return np.array(points)


def plot_3d_surface(points, points1, points2, points3, points4):
    plot1 = plt.figure(0, figsize=(10, 10))
    ax = plot1.add_subplot(projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='#9467bd', alpha=0.3)
    ax.scatter(points1[:, 0], points1[:, 1], points1[:, 2], color='red', alpha=0.5)
    ax.scatter(points2[:, 0], points2[:, 1], points2[:, 2], color='red', alpha=0.5)
    ax.scatter(points3[:, 0], points3[:, 1], points3[:, 2], color='#f542cb', alpha=0.5)
    ax.scatter(points4[:, 0], points4[:, 1], points4[:, 2], color='#f542cb', alpha=0.5)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    # ax1.scatter(points[:, 0], points[:, 1], points[:, 2], c=points[:, 2],  cmap='viridis', alpha=0.5)


def plot_projections(points):
    plot2, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))
    ax1.scatter(points[:, 1], points[:, 2], c=points[:, 2], cmap='viridis', zorder=3)
    ax2.scatter(points[:, 0], points[:, 2], c=points[:, 2], cmap='viridis', zorder=3)
    ax3.scatter(points[:, 0], points[:, 1], c=points[:, 2], cmap='viridis', zorder=3)
    ax1.grid(zorder=0)
    ax2.grid(zorder=0)
    ax3.grid(zorder=0)

    ax1.set_xlabel('Y')
    ax1.set_ylabel('Z')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Z')
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')


if __name__ == "__main__":
    u = np.arange(0.0, 1.0, 1.0/40)
    w = np.arange(0.0, 1.0, 1.0/40)

    P = np.array([[par_to_dec(np.array([0, 0])), par_to_dec(np.array([0, 1])), par_to_dec(P01(0, 0)), par_to_dec(P01(0, 1))],
                  [par_to_dec(np.array([1, 0])), par_to_dec(np.array([1, 1])), par_to_dec(P01(1, 0)), par_to_dec(P01(1, 1))],
                  [par_to_dec(P10(0, 0)), par_to_dec(P10(0, 1)), par_to_dec(P11(0, 0)), par_to_dec(P11(0, 1))],
                  [par_to_dec(P10(1, 0)), par_to_dec(P10(1, 1)), par_to_dec(P11(1, 0)), par_to_dec(P11(1, 1))]])

    points = find_points(u, w)
    points1 = find_points(np.zeros(1), w)
    points2 = find_points(np.ones(1), w)
    points3 = find_points(u, np.zeros(1))
    points4 = find_points(u, np.ones(1))

    plot_3d_surface(points, points1, points2, points3, points4)
    plot_projections(points)
    plt.show()
