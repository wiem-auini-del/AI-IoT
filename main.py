# main.py
"""
Smart temperature monitor with basic AI prediction.
Simulates IoT sensor readings, trains/uses a tiny model to predict next value,
and shows a simple plot.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import os

from model import train_model, load_model

DATA_FILE = "data/readings.csv"

def simulate_sensor(hours_count=24):
    """
    Simulate temperature readings for a given number of hours.
    """
    # Simple pattern: temp rises during day, drops at night, plus noise
    hours = np.arange(hours_count)
    temps = 10 + 0.5 * hours + np.random.randint(-3, 3, size=(hours_count,))
    return hours, temps

def save_readings(hours, temps):
    """
    Save simulated readings to CSV.
    """
    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame({
        "hour": hours,
        "temperature": temps,
        "timestamp": [datetime.now().isoformat()] * len(hours)
    })
    df.to_csv(DATA_FILE, index=False)
    print(f"Saved readings to {DATA_FILE}")

def plot_readings(hours, temps, predicted=None):
    plt.figure(figsize=(8, 4))
    plt.plot(hours, temps, label="Sensor readings")
    if predicted is not None:
        plt.scatter([hours[-1] + 1], [predicted], color='red', label="Prediction next hour")
    plt.xlabel("Hour")
    plt.ylabel("Temperature")
    plt.title("Temperature readings and prediction")
    plt.legend()
    plt.tight_layout()
    plt.show()

def run():
    # 1) simulate or load past readings
    hours, temps = simulate_sensor(24)

    # 2) save data
    save_readings(hours, temps)

    # 3) load or train model
    model = load_model()
    if model is None:
        model = train_model(hours, temps)
        print("Trained new model.")

    # 4) predict next hour temperature
    next_hour = np.array([[hours[-1] + 1]])
    prediction = model.predict(next_hour)[0]
    print(f"Predicted temperature for next hour: {prediction:.2f}")

    # 5) plot
    plot_readings(hours, temps, predicted=prediction)

if __name__ == "__main__":
    run()
