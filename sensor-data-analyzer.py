import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Simulated temperature sensor data
hours = np.array(range(24)).reshape(-1, 1)
temperature = 2 * hours + np.random.randint(-5, 5, size=(24,))

model = LinearRegression()
model.fit(hours, temperature)

pred = model.predict([[25]])

print("Predicted temperature next hour:", pred[0])

plt.plot(hours, temperature, label="Sensor data")
plt.plot(hours, model.predict(hours), label="AI Prediction")
plt.legend()
plt.show()
