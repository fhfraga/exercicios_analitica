import numpy as np
import matplotlib.pyplot as plt


def plates_theorical(A, B, C, u):
    """Calculates the height of the theoretical plates present in a chromatographic column

    Parameters
    ----------
    A : float
        peak widening by preferred paths
    B :float
        solute diffusion in the mobile phase
    C : float
        solute diffusion in the stationary phase
    u : float
        carrier gas speed

    Returns
    -------
    float
        equivalent height of a theoretical plate.
    """
    H = A + (B / u) + (C * u)
    return(H)


if __name__ == '__main__':
    H = plates_theorical(1.65, 25.8, 0.0236, np.arange(4, 102, 2))
    plt.figure(1, figsize=(6, 4))
    plt. plot(H, np.arange(4, 102, 2))
    plt.xlabel('Height of theoretical plates(mm)')
    plt.ylabel('Carrier gas speed(mL/min)')

    # save plot to file
    plt.savefig("Van Deemter's equation.pdf")

 # display plot on screen
    plt.show()
    print(H)