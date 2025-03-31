import numpy as np
from typing import Tuple

def resize_image(pixels: np.ndarray, new_size: Tuple[int, int], interpolation_radius = 1):
    alpha = False if (pixels.shape[2] == 3) else True

    if not alpha:
        new_pixels = [[(0, 0, 0) for _ in range(new_size[1])] for _ in range(new_size[0])]
    else:
        new_pixels = [[(0, 0, 0, 0) for _ in range(new_size[1])] for _ in range(new_size[0])]

    if interpolation_radius == 1:
        nearest_neighbor_interpolation(pixels, new_pixels, new_size)
    elif interpolation_radius == 2:
        bilinear_interpolation(pixels, new_pixels, new_size, alpha)
    elif interpolation_radius == 3:
        bicubic_interpolation(pixels, new_pixels, new_size)
    else:
        raise ValueError(f"Unknown interpolation_radius : {interpolation_radius}")

    return np.array(new_pixels, dtype=np.uint8)


def nearest_neighbor_interpolation(pixels : np.ndarray, new_pixels, new_size):
    step_x = (pixels.shape[0] - 1) / new_size[0]
    step_y = (pixels.shape[1] - 1) / new_size[1]

    for i in range(new_size[0]):
        x_ref = round(step_x * i)
        for j in range(new_size[1]):
            y_ref = round(step_y * j)
            new_pixels[i][j] = pixels[x_ref][y_ref]

def bilinear_interpolation(pixels: np.ndarray, new_pixels, new_size, alpha):
    step_x = (pixels.shape[0] - 1) / new_size[0]
    step_y = (pixels.shape[1] - 1) / new_size[1]

    for i in range(new_size[0] - 1):
        x_ref = round(step_x * i)
        for j in range(new_size[1] - 1):
            # main
            y_ref = round(step_y * j)
            new_pixels[i][j] =  interpolate_colors(alpha,
                pixels[x_ref][y_ref], pixels[x_ref][y_ref + 1], 
                pixels[x_ref + 1][y_ref], pixels[x_ref + 1][y_ref + 1]
            )
        # handle last index (special case)
        new_pixels[i][new_size[1] - 1] = interpolate_colors(alpha, 
            pixels[x_ref][y_ref], pixels[x_ref][y_ref - 1], 
            pixels[x_ref + 1][y_ref], pixels[x_ref + 1][y_ref - 1]
        )
    
    # handle last index (special case)
    for j in range(new_size[1] - 1):
        y_ref = round(step_y * j)
        new_pixels[i][j] = interpolate_colors(alpha, 
            pixels[x_ref][y_ref], pixels[x_ref][y_ref + 1], 
            pixels[x_ref - 1][y_ref], pixels[x_ref - 1][y_ref + 1]
        )
    new_pixels[i][new_size[1] - 1] = interpolate_colors(alpha, 
        pixels[x_ref][y_ref], pixels[x_ref][y_ref - 1], 
        pixels[x_ref - 1][y_ref], pixels[x_ref - 1][y_ref - 1]
    )

def bicubic_interpolation(pixels, size, new_pixels, new_size):
    step_x = (size[0] - 1) / new_size[0]
    step_y = (size[1] - 1) / new_size[1]

    pass


def interpolate_colors(alpha, *colors):
    k = 1 / len(colors)

    if not alpha:
        R = G = B = 0
        for color in colors:
            R += int(color[0])
            G += int(color[1])
            B += int(color[2])
        return (int(R * k), int(G * k), int(B * k))
    else:
        R = G = B = A = 0
        for color in colors:
            R += int(color[0])
            G += int(color[1])
            B += int(color[2])
            A += int(color[3])
        return (int(R * k), int(G * k), int(B * k), int(A * k))