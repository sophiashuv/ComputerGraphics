from mpl_toolkits.mplot3d import axes3d, Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


def par_to_dec(u_w):
    u, w = u_w
    x = u * (1 - w)
    y = w**4
    z = u**2
    return x, y, z


def dec_to_par(x, y, z):
    u = z**(1.0/2)
    w = y**(1.0/4)
    return np.array([u, w])


def Q(u, w):
    # x0, y0, z0 = par_to_dec(np.array([0, w]))
    # x1, y1, z1 = par_to_dec(np.array([1, w]))
    # x = x0 * (1 - u) + x1 * u
    # y = y0 * (1 - u) + y1 * u
    # z = z0 * (1 - u) + z1 * u
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
    # ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='#00b6b3', alpha=0.2)
    ax.scatter(points1[:, 0], points1[:, 1], points1[:, 2], color='#104348', alpha=0.7)
    # ax.scatter(points2[:, 0], points2[:, 1], points2[:, 2], color='#104348', alpha=0.7)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    # ax1.scatter(points[:, 0], points[:, 1], points[:, 2], c=points[:, 2],  cmap='viridis', alpha=0.5)


def plot_projections(points):
    plot2, (ax1, ax2, ax3) = plt.subplots(3, figsize=(4, 10))
    ax1.scatter(points[:, 1], points[:, 2], c=points[:, 2], cmap='PuBu', zorder=3)
    ax2.scatter(points[:, 0], points[:, 2], c=points[:, 2], cmap='PuBu', zorder=3)
    ax3.scatter(points[:, 0], points[:, 1], c=points[:, 2], cmap='PuBu', zorder=3)
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
    u = np.arange(0.0, 1.0, 1.0/20)
    w = np.arange(0.0, 1.0, 1.0/20)

    points = find_points(u, w)
    points1 = find_points(np.array([0.7]), w)
    # points1 = find_points(np.array([0, 1]), w)
    points2 = find_points(u, np.array([0, 1]))

    plot_3d_surface(points, points1, points2)
    plot_projections(points)
    plt.show()

    print(Q(3, 5))
    print(Q(7, 6))