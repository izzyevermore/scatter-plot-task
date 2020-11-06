import matplotlib.pyplot as plt
from matplotlib import *
import numpy as np

x = np.array([14.2, 16.5, 11.8, 15.3, 18.8, 22.5, 19.5])
y = np.array([220, 330, 190, 340, 410, 445, 415])

m, b = np.polyfit(x, y, 1)
plt.scatter(x, y, color="black")
plt.plot(x, m*x + b)
plt.plot(x, y, 'o')

plt.xlabel("Temperature")
plt.ylabel("Price in (R)")
plt.title("Soup sales in relation to temperature")
plt.show()
