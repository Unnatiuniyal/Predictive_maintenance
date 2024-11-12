**ABSTRACT**


This report presents a predictive maintenance analysis for Remaining Useful Life (RUL) prediction using the NASA Turbofan Engine Degradation Simulation Dataset. The primary objective of this study is to compare the performance of various machine learning models, including Linear Regression, Decision Trees, Random Forests, XGBoost, and LSTM (write full form), for accurate RUL prediction. The dataset was thoroughly explored, followed by data preprocessing techniques such as smoothing and cross-validation. Model performance was evaluated using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R-squared (R²). The results showed that ensemble methods such as Random Forest and XGBoost performed better than other models. The findings highlight the potential of machine learning techniques in predictive maintenance and suggest areas for future improvements in model accuracy and robustness.
Keywords: Predictive Maintenance, Remaining Useful Life (RUL), NASA Turbofan Engine Dataset, Machine Learning, Linear Regression, Decision Trees, Random Forest, XGBoost, LSTM, Data Preprocessing, Feature Engineering, Time Series Analysis, Multi-variate Analysis, Model Evaluation, MAE, RMSE, R², Model Comparison, Cross-validation, Smoothing Techniques.

**INTRODUCTION**

2.1 Overview of Predictive Maintenance and RUL Prediction


Predictive maintenance leverages data analytics and machine learning to anticipate equipment failures, enabling proactive interventions and minimizing unplanned downtime. Unlike reactive maintenance, which addresses issues post-failure, this strategy optimizes resources and reduces costs. A critical aspect is accurately predicting the Remaining Useful Life (RUL) of equipment, ensuring maintenance is scheduled effectively to maximize performance and avoid unnecessary repairs.


2.2 Problem Statement


Predict the Remaining Useful Life (RUL) of turbofan engines using time-series data from the NASA Turbofan Engine Degradation Simulation Dataset under varying operational conditions.


2.3 Project Objective and Scope


The objective of this project is to predict the Remaining Useful Life (RUL) of turbofan engines using the NASA Turbofan Engine Degradation Simulation Dataset. The focus is on assessing the performance of various models, including Linear Regression, XGBoost, and SVR to determine the most effective model for real-world predictive maintenance.


Scope:


1. Data exploration and preprocessing
2. Model training for RUL prediction
3. Model evaluation and comparative analysis


2.4 Uniqueness of the project


This project uniquely compares a range of models—Linear Regression, Random Forest, XGBoost, and SVR—for predicting Remaining Useful Life (RUL) of turbofan engines using the NASA dataset. Unlike studies focusing on single models, it combines time-series analysis, multivariate analysis, and advanced data preprocessing (smoothing, cross-validation) to enhance prediction accuracy. The practical focus is on real-world applicability, optimizing maintenance schedules, reducing costs, and minimizing downtime.


**Dataset Description**


Prognostics and health management (PHM) is a critical area in the industry, focusing on predicting the condition of assets to minimize unexpected downtime and failures. Accurate prognostics enable organizations to optimize maintenance schedules, improve safety, and reduce operational costs.

The NASA Turbofan Engine Degradation Simulation Dataset is a publicly available dataset for evaluating various machine learning techniques for RUL prediction. It simulates the performance and degradation of turbofan engines over time, capturing real-world operational complexities.The dataset includes time-series data from multiple engines, encompassing 21 sensor readings and 3 operational settings such as pressure, temperature, and rotational speed. These variables reflect the health status and degradation processes of the engines, enabling robust asset degradation modeling.
The dataset includes data from five rotating engine components: Fan, LPC, HPC, HPT, and LPT. Key gas path components are HPC, HPT, and LPT. Operational settings include altitude, throttle resolver angle (TRA), and Mach number. The time-series data captures measurements over cycles, simulating engine degradation until failure, making it ideal for Remaining Useful Life (RUL) prediction.
The primary challenge lies in accurately forecasting the RUL of engines by effectively capturing the complex degradation patterns, while accounting for non-linear sensor behaviour and varying operating conditions across different engines.



Source- Turbofan Engine Degradation Simulation Dataset

Note- The training, testing and Ground truth values of RUL are already provided in raw form in the train_FD001.txt, test_FD001.txt and RUL_FD001.txt

