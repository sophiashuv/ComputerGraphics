import math

import pygame
import numpy as np
from math import *

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("Petryshyn Maxim, Var 11")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

scale = 50
radius = 200
center = [WIDTH/2, HEIGHT/2]

angle = 0

cube_points = np.array([[-1, -1, 1],
                       [1, -1, 1],
                       [1,  1, 1],
                       [-1, 1, 1],
                       [-1, -1, -1],
                       [1, -1, -1],
                       [1, 1, -1],
                       [-1, 1, -1]])

tetrahedron_points = np.array([[0, -1, 0],
                               [1,  1, 1],
                               [-1, 1, 1],
                               [-1, 1, -1]])

projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
])


def connect_points(i, j, points):
    pygame.draw.line(screen, BLACK, (points[i][0], points[i][1]), (points[j][0], points[j][1]))


def point2d_projection(points, size, r, colour):
    projected_points = [[n, n] for n in range(len(points))]
    i = 0
    for point in points:
        rotated2d = np.dot(rotation_y, point.reshape((3, 1)))
        x = int(rotated2d[0][0] * size * scale) + r
        y = int(rotated2d[1][0] * size * scale) + center[1]
        z = int(rotated2d[2][0] * size * scale)

        rotated2d = np.dot(rotation_y, np.matrix([x, y, z]).reshape((3, 1)))
        projected2d = np.dot(projection_matrix, rotated2d)
        x = int(projected2d[0][0]) + center[0]
        y = int(projected2d[1][0])
        projected_points[i] = [x, y]
        pygame.draw.circle(screen, colour, (x, y), 5)
        i += 1
    return projected_points


if __name__ == "__main__":
    clock = pygame.time.Clock()
    size_cube = 1
    size_tetrahedron = 1
    while True:
        clock.tick(60)
        if angle % (math.pi * 2) < math.pi / 2 or math.pi + math.pi / 2 < angle % (math.pi * 2) < math.pi + math.pi:
            size_cube += 0.001
            size_tetrahedron -= 0.001
        else:
            size_cube -= 0.001
            size_tetrahedron += 0.001

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        rotation_y = np.matrix([
            [cos(angle), 0, sin(angle)],
            [0, 1, 0],
            [-sin(angle), 0, cos(angle)],
        ])

        angle += 0.01

        screen.fill(WHITE)
        pygame.draw.line(screen, BLACK, (WIDTH/2, 0), (WIDTH/2, HEIGHT))

        projected_points_cube = point2d_projection(cube_points, size_cube, radius, RED)
        projected_points_tetrahedron = point2d_projection(tetrahedron_points, size_tetrahedron, -radius, BLUE)

        for p in range(4):
            connect_points(p, (p + 1) % 4, projected_points_cube)
            connect_points(p + 4, ((p + 1) % 4) + 4, projected_points_cube)
            connect_points(p, (p + 4), projected_points_cube)

        for p in range(3):
            connect_points(p, (p + 1) % 3, projected_points_tetrahedron)
            connect_points(3, p, projected_points_tetrahedron)

        pygame.display.update()
