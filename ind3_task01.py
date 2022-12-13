from random import random


import numpy as np
import matplotlib.pyplot as plt

GRAY = np.array([166, 162, 162])
raster_x, raster_y = 32, 32
scale = 20


def generate_raster(size_x, size_y, scale):
    raster = np.zeros((size_x * scale, size_y * scale, 3)) + 255
    raster = raster.astype(int)
    return raster


def inter(x):
    dr = x - x.astype(int)

    dr[dr >= 0.5] = 1
    dr[dr <= -0.5] = -1
    dr[(dr < 0.5) & (dr > -0.5)] = 0
    x = x.astype(int) + dr
    return x


def get_angles_array(n, r):
    angles = np.arange(0, 360, 360/n)
    tan_angels = np.tan(np.deg2rad(angles))
    a = r * np.sin(np.deg2rad(angles))
    b = r * np.cos(np.deg2rad(angles))

    a = inter(a)
    b = inter(b)
    return angles, a, b


def check_sizes(coords_x, coords_y):
    if coords_y.shape[0] > coords_x.shape[0]:
        coords_x = np.append(coords_x, np.array([coords_x[-1]]))
    elif coords_y.shape[0] < coords_x.shape[0]:
        coords_y = np.append(coords_y, np.array([coords_y[-1]]))
    return coords_x, coords_y

def DDA_algorithm(a, b):
    if a == 0:
        coords_x = np.arange(1 if b > 0 else -1, b, 1 if b > 0 else -1)
        coords_y = np.zeros(int(abs(b) - 1))
    elif b == 0:
        coords_x = np.zeros(int(abs(a) - 1))
        coords_y = np.arange(1 if a > 0 else -1, a, 1 if a > 0 else -1)

    else:
        m = abs(a / b)
        if m > 1:
            step_x = 1/m if b > 0 else -1/m
            step_y = 1 if a > 0 else -1
            coords_x = np.arange(step_x, b + step_x, step_x)
            coords_y = np.arange(0, a, step_y)
        else:
            step_x = 1 if b > 0 else -1
            step_y = m if a > 0 else -m
            coords_x = np.arange(0, b, step_x)
            coords_y = np.arange(step_y, a + step_y, step_y)

        coords_x, coords_y = check_sizes(coords_x, coords_y)
        coords_x = inter(coords_x)
        coords_y = inter(coords_y)
    coords = np.vstack((coords_x, coords_y)).T
    return coords


def draw_raster(raster):
    raster[::scale] = GRAY
    raster[:, ::scale] = GRAY

    plt.figure(figsize=(10, 10))
    plt.axis("off")
    plt.imshow(raster.astype(np.uint8))
    plt.show()


def print_coords(angel, coords):
    print(f'{angel}°: {", ".join(f"({c[0]}, {c[1]})" for c in coords)}\n')


def draw_lines(angels, a, b):
    for i in range(len(angels)):
        color = np.array([int(random() * 255), int(random() * 255), int(random() * 255)])
        coords = DDA_algorithm(a[i], b[i])
        coords = coords + np.array([center_x, center_y])
        print_coords(angels[i], coords)

        for (x, y) in coords:
            raster[int(x) * scale: (int(x) + 1) * scale, int(y) * scale: (int(y) + 1) * scale] = color
        # draw_raster(raster)


if __name__ == "__main__":
    # center_x, center_y = (int(i) for i in input("Enter center coords: ").split(" "))
    # r = int(input("Enter r: "))
    # n = int(input("Enter lines amount: "))
    center_x, center_y = 10, 10
    r = 10
    n = 16

    raster = generate_raster(raster_x, raster_y, scale)

    angels, a, b = get_angles_array(n, r)
    draw_lines(angels, a, b)
    draw_raster(raster)



