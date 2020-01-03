import numpy as np
import matplotlib.pyplot as plt


def pratos_teoricos(A, B, C, u):
    """Calcula a altura dos pratos teóricos presentes
    em uma coluna cromatografica

    Parameters
    ----------
    A : float
        alargamento de picos por caminhos preferenciais
    B :float
        difusão do soluto na fase móvel
    C : float
        difusão do soluto na fase móvel
    u : float
        velocidade do gás de arraste

    Returns
    -------
    float
        altura equivalente a um prato teórico.
    """
    H = A + (B / u) + (C * u)
    return(H)


if __name__ == '__main__':
    H = pratos_teoricos(1.65, 25.8, 0.0236, np.arange(4, 102, 2))
    grafico = plt.plot(H, np.arange(4,102,2))
    print(H, grafico)
    