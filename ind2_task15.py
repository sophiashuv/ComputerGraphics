from mpl_toolkits.mplot3d import axes3d, Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


def par_to_dec(u_w):
    u, w = u_w
    x = u * (1 - w)
    y = w
    z = u
    return x, y, z


def Q(u, w):
    p1 = np.array([0, w])
    p2 = np.array([1, w])
    q = p1*(1-u) + p2*u
    x, y, z = par_to_dec(q)
    return np.array([x, y, z])


def find_points(u, w):
    points = []
    for uu in u:
        for ww in w:
            points.append(Q(uu, ww))
    return np.array(points)


def plot_3d_surface(points, points1, points2):
    plot1 = plt.figure(0, figsize=(7, 7))
    ax = plot1.add_subplot(projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='#ff4527', alpha=0.7, s=1)
    ax.scatter(points1[:, 0], points1[:, 1], points1[:, 2], color='#ff9429', alpha=0.7)
    ax.scatter(points2[:, 0], points2[:, 1], points2[:, 2], color='#ff9429', alpha=0.7)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')


def plot_projections(points):
    plot2, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 4))
    ax1.scatter(points[:, 1], points[:, 2], c=points[:, 2], cmap='OrRd', zorder=3, s=1)
    ax2.scatter(points[:, 0], points[:, 2], c=points[:, 2], cmap='OrRd', zorder=3, s=1)
    ax3.scatter(points[:, 0], points[:, 1], c=points[:, 2], cmap='OrRd', zorder=3, s=1)
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
    u = np.arange(0.0, 1.0, 1.0/100)
    w = np.arange(0.0, 1.0, 1.0/100)

    points = find_points(u, w)
    points1 = find_points(np.array([0, 1]), w)
    points2 = find_points(u, np.array([0, 1]))

    plot_3d_surface(points, points1, points2)
    plot_projections(points)
    plt.show()
