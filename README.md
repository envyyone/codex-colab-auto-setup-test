# Codex + Google Colab First Test Project

This repository is a tiny beginner-friendly Colab project for **temperature vs reaction rate** analysis.

## Project structure

- `requirements.txt`
- `src/simple_analysis.py`
- `notebooks/first_colab_analysis.ipynb`
- `outputs/.gitkeep`

## What the notebook does

1. Runs an important setup cell (first code cell) that:
   - clones this repository in Colab if needed,
   - changes directory to the repository root,
   - installs `requirements.txt`,
   - makes local `src/` code importable.
2. Generates fake experimental data (`temperature_C` and `rate`).
3. Fits a simple linear model.
4. Prints the equation:
   - `rate = a * temperature_C + b`
5. Predicts the reaction rate at **500 °C**.
6. Saves a plot to `outputs/temperature_vs_rate.png`.

## Using this notebook with a private GitHub repo

1. Create a **fine-grained GitHub personal access token**.
2. Grant it **read-only Contents access** to this repository (`envyyone/codex-colab-auto-setup-test`).
3. Open the notebook in Google Colab.
4. In Colab, open the **Secrets** panel and add a secret named **`GITHUB_TOKEN`**.
5. Paste your token as the secret value and **enable notebook access**.
6. Click **Runtime → Run all**.

The notebook setup cell will read `GITHUB_TOKEN` from Colab Secrets and clone the private repository securely (without hard-coding or printing your token).

## How to run in Google Colab

1. Open `notebooks/first_colab_analysis.ipynb` from GitHub in Google Colab.
2. In Colab, click **Runtime → Run all**.
3. The first cell automatically prepares everything.

## Expected outputs

- A displayed dataframe of fake data.
- Printed linear equation coefficients.
- Predicted rate at 500 °C.
- Saved plot file at `outputs/temperature_vs_rate.png`.
