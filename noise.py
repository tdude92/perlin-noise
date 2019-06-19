import numpy
import random

# Gradient vectors
vector_table = (
    numpy.array([1, 1]),
    numpy.array([1, -1]),
    numpy.array([-1, -1]),
    numpy.array([-1, 1])
)

def fade(x):
    # Fade function
    return 6*x**5 - 15*x**4 + 10*x**3

def perlin_noise(sec_x, sec_y, sec_width = 5, sec_length = 5):
    # Args:
    #   sec_x (int): number of sections wide.
    #   sec_y (int): number of sections long.
    #   sec_width (int): how many pixels wide a section is.
    #   sec_length (int): how many pixels long a section is.

    # Returns: 2d array of values.

    out = [[] for _ in range(sec_y * sec_length)]
    all_gradient_vectors = [[random.choice(vector_table) for i in range(sec_x + 1)] for j in range(sec_y + 1)]

    for i in range(sec_y):
        for j in range(sec_x):
            # Define vectors.
            # Vector order: top left, top right, bottom right, bottom left.
            gradient_vectors = [
                all_gradient_vectors[i][j],
                all_gradient_vectors[i][j + 1],
                all_gradient_vectors[i + 1][j + 1],
                all_gradient_vectors[i + 1][j]
            ]
            for y in range(sec_length):
                y += 1
                for x in range(sec_width):
                    x += 1
                    frac_x = (x - 1) / (sec_width - 1)
                    frac_y = (y - 1) / (sec_width - 1)

                    distance_vectors = [
                        numpy.array([frac_x, frac_y]),
                        numpy.array([-(1 - frac_x), frac_y]),
                        numpy.array([-(1 - frac_x), -(1 - frac_y)]),
                        numpy.array([frac_x, -(1 - frac_y)])
                    ]

                    # Get dot products.
                    dots = [numpy.dot(gradient_vectors[i], distance_vectors[i]) for i in range(4)]

                    # Linear interpolation.
                    AB = dots[0] + frac_x * (dots[1] - dots[0])
                    CD = dots[3] + frac_x * (dots[2] - dots[3])
                    value = AB + frac_y * (CD - AB)
                    out[i * sec_length + y - 1].append(fade(value))
    return out

if __name__ == "__main__":
    for i in perlin_noise(2, 2):
        print(i)
