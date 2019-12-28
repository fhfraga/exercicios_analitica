import numpy as np
import matplotlib.pyplot as plt

def pratos_teoricos(A, B, C, u):
    H = A + (B / u) + (C * u)
    return(H)

if __name__ == '__main__':
    H = pratos_teoricos(1.65, 25.8, 0.0236, np.arange(4, 102, 2))
    grafico = plt.plot(H, np.arange(4,102,2))
    print(H, grafico)




