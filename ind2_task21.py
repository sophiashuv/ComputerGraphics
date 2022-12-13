from mpl_toolkits.mplot3d import axes3d, Axes3D
import matplotlib.pyplot as plt
import numpy as np


def FU(t):
    T = np.array([t ** 3, t ** 2, t, 1])
    res = np.matmul(M, T)
    return res


def FW(t):
    T = np.array([t ** 3, t ** 2, t, 1])
    A = M.transpose()
    res = np.matmul(A, T)
    return res


def Q(u, w):
    # vec1 = np.array([(1-u)**3, 3*u*(1-u)**2, 3*u**2*(1-u), u**3])
    # vec2 = np.array([(1-w)**3, 3*w*(1-w)**2, 3*w**2*(1-w), w**3])
    x = np.matmul(np.matmul(B[:, :, 0], FU(u)), FW(w))
    y = np.matmul(np.matmul(B[:, :, 1], FU(u)), FW(w))
    z = np.matmul(np.matmul(B[:, :, 2], FU(u)), FW(w))

    return np.array([x, y, z])


def find_points(u, w):
    points = []
    for uu in u:
        for ww in w:
            points.append(Q(uu, ww))
    return np.array(points)


def plot_3d_surface(points, points1, points2, points3, points4, B):
    plot1 = plt.figure(0, figsize=(10, 10))
    ax = plot1.add_subplot(projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='deeppink', alpha=0.3)
    ax.scatter(points1[:, 0], points1[:, 1], points1[:, 2], color='purple', alpha=0.5)
    ax.scatter(points2[:, 0], points2[:, 1], points2[:, 2], color='purple', alpha=0.5)
    ax.scatter(points3[:, 0], points3[:, 1], points3[:, 2], color='blueviolet', alpha=0.5)
    ax.scatter(points4[:, 0], points4[:, 1], points4[:, 2], color='blueviolet', alpha=0.5)

    ax.plot(B[0][:, 0], B[0][:, 1], B[0][:, 2], color='blue', alpha=0.5)
    ax.scatter(B[0][:, 0], B[0][:, 1], B[0][:, 2], color='blue', alpha=0.5)
    ax.plot(B[1][:, 0], B[1][:, 1], B[1][:, 2], color='blue', alpha=0.5)
    ax.scatter(B[1][:, 0], B[1][:, 1], B[1][:, 2], color='blue', alpha=0.5)
    ax.plot(B[2][:, 0], B[2][:, 1], B[2][:, 2], color='blue', alpha=0.5)
    ax.scatter(B[2][:, 0], B[2][:, 1], B[2][:, 2], color='blue', alpha=0.5)
    ax.plot(B[3][:, 0], B[3][:, 1], B[3][:, 2], color='blue', alpha=0.5)
    ax.scatter(B[3][:, 0], B[3][:, 1], B[3][:, 2], color='blue', alpha=0.5)

    ax.plot(B[:, 0, 0], B[:, 0, 1], B[:, 0, 2], color='blue', alpha=0.5)
    ax.plot(B[:, 1, 0], B[:, 1, 1], B[:, 1, 2], color='blue', alpha=0.5)
    ax.plot(B[:, 2, 0], B[:, 2, 1], B[:, 2, 2], color='blue', alpha=0.5)
    ax.plot(B[:, 3, 0], B[:, 3, 1], B[:, 3, 2], color='blue', alpha=0.5)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')


def plot_projections(points):
    plot2, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))
    ax1.scatter(points[:, 1], points[:, 2], c=points[:, 2], cmap='magma_r', zorder=3)
    ax2.scatter(points[:, 0], points[:, 2], c=points[:, 2], cmap='magma_r', zorder=3)
    ax3.scatter(points[:, 0], points[:, 1], c=points[:, 2], cmap='magma_r', zorder=3)
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
    u = np.arange(0.0, 1.0, 1.0 / 70)
    w = np.arange(0.0, 1.0, 1.0 / 70)

    M = np.array([[-1, 3, -3, 1],
                  [3, -6, 3, 0],
                  [-3, 3, 0, 0],
                  [1, 0, 0, 0]])

    B = np.array([[[-15, 0, 15], [-15, 5, 5], [-15, 5, -5], [-15, 0, -15]],
                  [[-5, 5, 15], [-5, 5, 5], [-5, 5, -5], [-5, 5, -15]],
                  [[5, 5, 15], [5, 5, 5], [5, 5, -5], [5, 5, -15]],
                  [[15, 0, 15], [15, 5, 5], [15, 5, -5], [15, 0, -15]]])

    points = find_points(u, w)
    points1 = find_points(np.zeros(1), w)
    points2 = find_points(np.ones(1), w)
    points3 = find_points(u, np.zeros(1))
    points4 = find_points(u, np.ones(1))

    plot_3d_surface(points, points1, points2, points3, points4, B)
    plot_projections(points)
    plt.show()
