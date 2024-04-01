Combined Cycle Power Plant Energy Production Modeling

Overview :

This repository contains code and resources for modeling energy production in a combined cycle power plant. The objective of this project is to develop a predictive model that estimates net hourly electrical energy output based on various ambient and operational variables.

Dataset :

The dataset used for this project contains 9568 observations collected over six years from a combined cycle power plant operating at full load. The variables in the dataset are as follows:

Temperature: Temperature in degrees Celsius.

Exhaust Vacuum: Vacuum level in cm Hg.

Ambient Pressure: Ambient pressure in millibar.

Relative Humidity: Relative humidity as a percentage.

Energy Production: Net hourly electrical energy output in MW.

Approach :

Data Exploration: Exploratory data analysis was performed to understand the distribution of variables, identify correlations, and detect any anomalies.

Feature Engineering: Features were scaled and normalized, and additional features such as interactions were created to improve model performance.

Model Selection: Several regression algorithms were evaluated, including Linear Regression, Random Forest Regression, and Gradient Boosting Regression. Hyperparameters were tuned using cross-validation to optimize model performance.

Model Training and Evaluation: The selected model was trained on the training dataset and evaluated using metrics such as mean squared error (MSE) and mean absolute error (MAE) on the test dataset.

Model Deployment: Once the model demonstrated satisfactory performance, it was deployed in the production environment for real-time predictions.

Files :

combined_cycle_power_plant.csv: The dataset used for modeling energy production.

modeling.ipynb: Jupyter Notebook containing code for data preprocessing, model training, and evaluation.

requirements.txt: List of Python packages required to run the code.
