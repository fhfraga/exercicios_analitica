import numpy as np
import matplotlib.pyplot as plt


def plates_theorical(A, B, C, u):
    """Calculates the height of the theoretical plates present in a
    chromatographic column

    Parameters
    ----------
    A : float
        Eddy-diffusion parameter, related to channeling through a non-ideal
        packing. Dimension L
    B :float
         diffusion coefficient of the eluting particles in the longitudinal
         direction, resulting in dispersion. Dimension L^2 / T
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
    plt.style.use('seaborn-whitegrid')
    plt.plot(H, np.arange(4, 102, 2))
    plt.xlabel('Height of theoretical plates / (mm)')
    plt.ylabel('Carrier gas speed / (mL/min)')
    plt.tight_layout()  # avoids cutting labels depending on style

    # save plot to file
    plt.savefig("Van Deemter's equation.pdf")

    # display plot on screen
    plt.show()
    # print(H)  # activate for values
