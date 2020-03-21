import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

protein = np.array([0.00, 9.36, 18.72, 28.08, 37.44]).reshape((-1, 1))
absorbance = np.array([0.466, 0.676, 0.883, 1.086, 1.280])

model = LinearRegression()
model.fit(protein, absorbance)
model = LinearRegression().fit(protein, absorbance)
r_sq = model.score(protein, absorbance)
new_model = LinearRegression().fit(protein, absorbance.reshape((-1, 1)))
absorbance_pred = model.predict(protein)

if __name__ == "__main__":
    plt.scatter(protein, absorbance, color = 'black')
    plt.plot(protein, absorbance_pred,color = 'blue', linewidth = 3)
    plt.savefig("linear_regression.png")
    plt.show()
