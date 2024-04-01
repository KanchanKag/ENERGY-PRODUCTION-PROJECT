import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the trained Random Forest model
#model = pickle.load(open('random_forest_model.pkl', "rb"))
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the Streamlit app
def main():
    # Set title and description
    st.title('Energy Production Prediction')
    st.write('Enter the values of the features to predict energy production.')

    # Add explanatory text and images
    #st.image('your_image_path.jpg', use_column_width=True)
    st.write('This app predicts energy production based on temperature, exhaust vacuum, ambient pressure, and relative humidity.')

    # Add sidebar
    st.sidebar.title('Settings')
    st.sidebar.write('Adjust the input values below:')

    # Input fields for features
    temperature = st.sidebar.slider('Temperature (degrees Celsius)', min_value=-1.0, max_value=40.0)
    exhaust_vacuum = st.sidebar.slider('Exhaust Vacuum (cm Hg)', min_value=10.0, max_value=100.0)
    amb_pressure = st.sidebar.slider('Ambient Pressure (millibar)', min_value=900.0, max_value=1500.0)
    r_humidity = st.sidebar.slider('Relative Humidity (%)', min_value=10, max_value=100)

    # Make prediction when 'Predict' button is clicked
    if st.sidebar.button('Predict'):
        # Preprocess input features and make prediction
        features = [temperature, exhaust_vacuum, amb_pressure, r_humidity]
        prediction = model.predict(np.array(features).reshape(1, -1))[0]

        # Display prediction
        st.write(f'Predicted Energy Production: {prediction} MW')



# Run the Streamlit app
if __name__ == '__main__':
    main()
