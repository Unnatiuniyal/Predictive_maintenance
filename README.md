# Predictive Maintenance Analysis for Remaining Useful Life (RUL) Prediction

This project implements a predictive maintenance model to estimate the Remaining Useful Life (RUL) of turbofan engines using machine learning techniques. The analysis is based on the **NASA Turbofan Engine Degradation Simulation Dataset** and compares various algorithms, including Linear Regression, Decision Trees, Random Forest, XGBoost, and Long Short-Term Memory (LSTM) neural networks, for effective RUL prediction.

## Project Overview

Predictive maintenance uses data analytics to forecast equipment failures, helping to schedule maintenance proactively and avoid unexpected downtime. This project focuses on accurate RUL prediction to ensure timely maintenance, minimize costs, and improve asset performance.

### Key Objectives
- Predict the RUL of turbofan engines under varying conditions.
- Evaluate and compare models, including Linear Regression, Random Forest, XGBoost, and SVR, for RUL prediction.
- Employ data preprocessing techniques, such as smoothing and cross-validation, to enhance model accuracy.

### Uniqueness of the Project
This project explores a diverse set of models to determine the optimal approach for predicting RUL, with a practical focus on minimizing downtime and maintenance costs. By combining time-series and multivariate analysis with advanced preprocessing methods, the project aims to achieve robust predictions applicable to real-world scenarios.

## Dataset

### Description

The NASA Turbofan Engine Degradation Simulation Dataset simulates the degradation of turbofan engines under various operating conditions, capturing sensor data and operational settings over time. The dataset includes:
- **21 sensor measurements** reflecting engine condition.
- **3 operational settings**: altitude, throttle resolver angle (TRA), and Mach number.
- **Data from 5 key engine components**: Fan, LPC, HPC, HPT, and LPT (High-Pressure Compressor, High-Pressure Turbine, and Low-Pressure Turbine).

The dataset is organized into four subsets (FD001–FD004), each representing different experimental scenarios:

| Dataset | Train Trajectories | Test Trajectories | Conditions | Fault Modes |
| ------- | ------------------ | ----------------- | ---------- | ----------- |
| FD001   | 100                | 100               | 1 (Sea Level) | 1 (HPC Degradation) |
| FD002   | 260                | 259               | 6              | 1 (HPC Degradation) |
| FD003   | 100                | 100               | 1 (Sea Level) | 2 (HPC and Fan Degradation) |
| FD004   | 248                | 249               | 6              | 2 (HPC and Fan Degradation) |

Each dataset contains multivariate time series from individual engines. Each engine operates normally at the beginning, and degradation leads to failure over time.

### Columns in the Dataset
1. `unit number`: Unique engine identifier
2. `time, in cycles`: Operational cycle count
3. `operational setting 1`
4. `operational setting 2`
5. `operational setting 3`
6. `sensor measurement 1` to `sensor measurement 26`: Measurements of engine parameters

**Reference**: A. Saxena, K. Goebel, D. Simon, and N. Eklund, "Damage Propagation Modeling for Aircraft Engine Run-to-Failure Simulation," in Proceedings of the 1st International Conference on Prognostics and Health Management (PHM08), Denver CO, Oct 2008.

## Methodology

### Data Preprocessing
- **Smoothing Techniques**: Applied to reduce noise in sensor data.
- **Cross-Validation**: Implemented for reliable model performance estimation.

### Models Used
1. **Linear Regression**
2. **RandomizedSearchCV and ElasticNet with reduced cross-validation**
3. **Random Forest**
4. **XGBoost**

### Model Evaluation
Models were evaluated based on:
- **Root Mean Squared Error (RMSE)**
- **R-squared (R²)**

### Findings
Ensemble methods, particularly **Random Forest** and **XGBoost**, outperformed other models in predicting RUL accurately. These results highlight the value of machine learning in predictive maintenance and suggest future improvements in model robustness and generalizability.

## Streamlit App

A Streamlit app is available in this repository to demonstrate the model's predictive capabilities interactively. It allows users to input operational settings and sensor measurements to predict the RUL of an engine.


## Repository Structure
- `app.py`: Streamlit application for interactive RUL prediction.
- `forest_regression.sav`: Trained RandomForest model for RUL prediction.
- `data/`: Folder containing dataset files.
- `notebooks/`: Jupyter notebooks for model training and analysis.
- `README.md`: Project overview and documentation.

## Keywords
Predictive Maintenance, Remaining Useful Life (RUL), NASA Turbofan Engine Dataset, Machine Learning, Linear Regression, Decision Trees, Random Forest, XGBoost, LSTM, Data Preprocessing, Feature Engineering, Time Series Analysis, Model Evaluation, Cross-validation, Smoothing Techniques.

---

Explore the potential of machine learning in predictive maintenance and gain insights into effective RUL prediction for turbofan engines.
