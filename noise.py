import numpy
import random

grid_width = 20
grid_height = 20
section_width = 5
section_length = 5

# Gradient vectors
vector_table = (
    numpy.array([1, 1]),
    numpy.array([1, -1]),
    numpy.array([-1, -1]),
    numpy.array([-1, 1])
)

def fade(x):
    return 6*x**5 - 15*x**4 + 10*x**3

def perlin_noise(sec_x, sec_y):
    # Args:
    #   sec_x (int): number of sections wide.
    #   sec_y (int): number of sections long.
    # Returns: 2d array of values.

    out = [[] for _ in range(sec_y * section_length)]

    for i in range(sec_y):
        for j in range(sec_x):
            # Define vectors.
            # Vector order: top left, top right, bottom right, bottom left.
            gradient_vectors = [
                random.choice(vector_table),
                random.choice(vector_table),
                random.choice(vector_table),
                random.choice(vector_table)
            ]
            for y in range(section_length):
                y += 1
                for x in range(section_width):
                    x += 1
                    frac_x = (x - 1) / (section_width - 1)
                    frac_y = (y - 1) / (section_width - 1)

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
                    out[i * section_length + y - 1].append(value)
    return out

if __name__ == "__main__":
    for i in perlin_noise(2, 2):
        print(i)
