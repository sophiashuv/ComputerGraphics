import numpy as np
import math
import matplotlib.pyplot as plt


def funk(X, Y, points, p):
    res = 1
    for (x, y) in points:
        res *= ((x - X)**2 + (y - Y)**2)
    return res - p**2


def input_data():
    m = int(input("Enter m: "))
    p = float(input("Enter p: "))
    return m, p


def create_meshgrid(p, points_range):
    x = np.linspace(-p - math.sqrt(2.0) * points_range[1], p + math.sqrt(2.0) * points_range[1], 10000)
    y = np.linspace(-p - math.sqrt(2.0) * points_range[1], p + math.sqrt(2.0) * points_range[1], 10000)
    X, Y = np.meshgrid(x, y)
    return X, Y


def draw_plot(X, Y, F, generated_points, e):
    plt.figure(figsize=(10, 10))
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(zorder=0)

    plt.plot(generated_points[:, 0], generated_points[:, 1], 'o', color='red')
    for (x, y) in generated_points:
        label = f"({round(x, 2)},{round(y, 2)})"
        plt.annotate(label,
                     (x, y),
                     textcoords="offset points",
                     xytext=(0, 10),
                     ha='center')

    plt.contour(X, Y, F, [0])
    plt.plot(X[(F > -e) & (F < e)], Y[(F > -e) & (F < e)], 'o', color='blue')
    plt.show()


if __name__ == "__main__":
    points_range = (0, 1)
    e = 0.0001
    m, p = input_data()
    generated_points = np.random.uniform(low=points_range[0], high=points_range[1], size=(m, 2))
    X, Y = create_meshgrid(p, points_range)

    F = funk(X, Y, generated_points, p)
    draw_plot(X, Y, F, generated_points, e)

