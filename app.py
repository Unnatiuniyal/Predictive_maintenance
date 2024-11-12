# Import necessary libraries
import streamlit as st
import joblib
import pandas as pd

# Load the saved RandomForest model
model_path = '/mnt/data/forest_regression.sav'
model = joblib.load(model_path)

# Define the main function for the Streamlit app
def main():
    # Title and introduction
    st.title("Predictive Maintenance Model for Engine RUL Prediction")
    st.write("This app predicts the Remaining Useful Life (RUL) for engines based on input features.")

    # Input fields for operational settings and sensor measurements
    st.header("Input Engine Operational Settings and Sensor Measurements")

    # Operational settings inputs
    operational_setting_1 = st.number_input("Operational Setting 1", min_value=0.0, max_value=100.0, value=50.0)
    operational_setting_2 = st.number_input("Operational Setting 2", min_value=0.0, max_value=100.0, value=50.0)
    operational_setting_3 = st.number_input("Operational Setting 3", min_value=0.0, max_value=100.0, value=50.0)

    # Sensor measurements (26 sensors)
    sensor_values = []
    for i in range(1, 27):
        sensor_val = st.number_input(f"Sensor Measurement {i}", min_value=0.0, max_value=100.0, value=50.0)
        sensor_values.append(sensor_val)

    # Collect all inputs into a DataFrame
    input_data = pd.DataFrame({
        'operational_setting_1': [operational_setting_1],
        'operational_setting_2': [operational_setting_2],
        'operational_setting_3': [operational_setting_3],
        **{f'sensor_{i}': [sensor_values[i-1]] for i in range(1, 27)}
    })

    # Run prediction
    if st.button("Predict RUL"):
        # Predict using the model
        prediction = model.predict(input_data)
        # Display the prediction
        st.write(f"Predicted Remaining Useful Life (RUL): {prediction[0]:.2f}")

# Run the app
if __name__ == "__main__":
    main()
