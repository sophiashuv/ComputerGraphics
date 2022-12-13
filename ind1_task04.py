import pygame
import numpy as np
from math import *


WIDTH, HEIGHT = 700, 700

speed = 2
step = 0.05
defSize = 300

pygame.display.set_caption("Pasha Zabavskiy, Var 4")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

rotation_matrix = lambda alpha: np.array([
    [cos(alpha), -sin(alpha)],
    [sin(alpha), cos(alpha)]])


def draw_rotated_rectangle(rectangle_points, ang, color, center_coords):
    rotated_points = np.dot(rectangle_points, rotation_matrix(ang).T)
    rotated_points += center_coords
    pygame.draw.polygon(screen, color, rotated_points)


def get_half_rect_length(alpha, len):
    s = sin(alpha)
    c = cos(alpha)

    if s < 0:
        s = -s
    if c < 0:
        c = -c
    return len / (2 * (s + c))


if __name__ == "__main__":
    clock = pygame.time.Clock()
    frameCount = 0
    alpha = 10

    while True:
        clock.tick(20)

        if frameCount % speed == 0:
            color = (frameCount * 3 % 255, frameCount * 5 % 255, frameCount * 7 % 255)

            if alpha >= 1.65:
                alpha = 0

            a = get_half_rect_length(alpha, defSize)

            centered_rectangle_coords = np.array(
                [[-a, -a],
                 [a, -a],
                 [a, a],
                 [-a, a]])

            draw_rotated_rectangle(centered_rectangle_coords, alpha, color, np.array([200, 200]))
            draw_rotated_rectangle(centered_rectangle_coords, -alpha, color, np.array([200, 500]))
            draw_rotated_rectangle(centered_rectangle_coords, -alpha, color, np.array([500, 200]))
            draw_rotated_rectangle(centered_rectangle_coords, alpha, color, np.array([500, 500]))

        pygame.display.update()
        frameCount += 1
        alpha += step
