from turtle import color
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
n= 100
xpoints = np.linspace(0,2*math.pi,n).reshape(-1,1)
ypoints = np.sin(xpoints)
linreg = LinearRegression()
linreg.fit(xpoints, ypoints)
y_pred = linreg.predict(xpoints)
plt.scatter(xpoints, ypoints, color='red')
plt.plot(xpoints, y_pred)
plt.show()
