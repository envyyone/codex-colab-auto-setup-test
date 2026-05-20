"""Simple analysis utilities for a beginner-friendly Colab project."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def generate_fake_data(seed: int = 0) -> pd.DataFrame:
    """Generate fake temperature vs. reaction-rate data with small noise."""
    rng = np.random.default_rng(seed)
    temperature = np.arange(300, 801, 50)
    noise = rng.normal(loc=0.0, scale=0.8, size=temperature.size)
    rate = 0.12 * temperature - 20 + noise
    return pd.DataFrame({"temperature_C": temperature, "rate": rate})


def fit_linear_model(df: pd.DataFrame) -> LinearRegression:
    """Fit a linear regression model to the data frame."""
    model = LinearRegression()
    x = df[["temperature_C"]]
    y = df["rate"]
    model.fit(x, y)
    return model


def predict_rate(model: LinearRegression, temperature: float) -> float:
    """Predict reaction rate at a given temperature."""
    prediction = model.predict(np.array([[temperature]]))
    return float(prediction[0])


def save_plot(df: pd.DataFrame, model: LinearRegression, output_path: str | Path) -> None:
    """Save a scatter plot with fitted line to disk."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    x = df["temperature_C"].to_numpy().reshape(-1, 1)
    y = df["rate"].to_numpy()

    x_line = np.linspace(df["temperature_C"].min(), df["temperature_C"].max(), 200).reshape(-1, 1)
    y_line = model.predict(x_line)

    plt.figure(figsize=(7, 4.5))
    plt.scatter(x, y, label="Fake data", color="steelblue")
    plt.plot(x_line, y_line, label="Linear fit", color="darkorange")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Reaction rate")
    plt.title("Temperature vs Reaction Rate")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
