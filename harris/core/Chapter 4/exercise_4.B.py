import numpy as np
import statistics


def statistical_function(a, b, c, d, e):
    x = np.array([a, b, c, d])
    return(x)


if __name__ == "__main__":

    x = statistical_function(17.4, 18.1, 18.2, 17.9, 17.6)
    mean = x.mean()

    array_mean = x - mean

    array_mean_square = array_mean** 2

    standard_deviation = statistics.stdev(x)

    print(x.sum())
    print(array_mean)
    print(array_mean_square)
    print(standard_deviation)
