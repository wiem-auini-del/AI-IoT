# model.py
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

MODEL_FILE = "temp_model.joblib"

def train_model(hours, temps):
    """
    Train a simple linear regression model.
    """
    model = LinearRegression()
    model.fit(hours.reshape(-1, 1), temps)
    joblib.dump(model, MODEL_FILE)
    return model

def load_model():
    """
    Load the trained model if exists, else None.
    """
    try:
        return joblib.load(MODEL_FILE)
    except:
        return None
