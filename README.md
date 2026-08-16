# City Energy Consumption Analysis & Prediction System

## 📌 About the Project

This project was developed as part of my Data Science internship task.

The aim of the project is to analyze electricity consumption patterns across different city zones and build a Machine Learning model to predict the next day's electricity demand.

A synthetic dataset containing **365 days of data for 5 city zones** was generated using Python.

---

## 🎯 Objective

The main objectives of this project are:

* Generate a realistic synthetic electricity consumption dataset.
* Clean and preprocess the data.
* Analyze electricity consumption across different zones.
* Study the effect of temperature, humidity, and special events on energy demand.
* Visualize important consumption patterns.
* Build a Machine Learning model for next-day energy prediction.
* Evaluate the model using Mean Absolute Error (MAE).
* Create an interactive prediction system with input validation.

---

## 📊 Dataset

The synthetic dataset contains **1,825 records** representing 365 days across 5 city zones.

### Features

| Feature           | Description                     |
| ----------------- | ------------------------------- |
| Date              | Date of electricity consumption |
| ZoneID            | City zone from Z1 to Z5         |
| AvgTemperature    | Average daily temperature in °C |
| Humidity          | Daily humidity percentage       |
| SpecialEvent      | 0 = No event, 1 = Special event |
| EnergyConsumption | Electricity consumed in kWh     |

For next-day prediction, additional features were created using the following day's temperature, humidity, event information, and energy consumption.

---

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Google Colab
* GitHub

---

## 🔄 Project Workflow

1. Imported the required Python libraries.
2. Generated synthetic data for 365 days and 5 zones.
3. Performed data cleaning and validation.
4. Checked missing values and duplicate records.
5. Performed exploratory data analysis.
6. Calculated monthly and zone-wise electricity consumption.
7. Analyzed event and non-event electricity usage.
8. Created data visualizations.
9. Prepared features for next-day prediction.
10. Split the dataset into training and testing sets.
11. Trained a Linear Regression model.
12. Evaluated the model using MAE.
13. Developed an interactive prediction system.
14. Added input validation and error handling.

---

## 📈 Data Visualizations

Three major visualizations were created:

### 1. Monthly Energy Consumption by Zone

Shows how average electricity consumption changes across months for different city zones.

### 2. Correlation Heatmap

Shows the relationship between temperature, humidity, special events, and electricity consumption.

### 3. Event vs Non-Event Consumption

Compares average electricity demand on special-event days and normal days.

---

## 🤖 Machine Learning Model

A **Linear Regression** model was used to predict next-day electricity consumption.

The model uses:

* Zone
* Tomorrow's temperature
* Tomorrow's humidity
* Tomorrow's special-event indicator

to predict:

**Tomorrow's Energy Consumption (kWh)**

The dataset was divided into **80% training data and 20% testing data**.

---

## 📏 Model Evaluation

The model was evaluated using **Mean Absolute Error (MAE)**.

**MAE: 51.75 kWh**

This means that, on average, the model's predicted electricity consumption differs from the actual value by approximately **51.75 kWh** on the synthetic test data.

---

## 🔍 Key Insights

* Average electricity consumption on **non-event days** was approximately **2158.51 kWh**.
* Average electricity consumption on **special-event days** increased to approximately **2361.74 kWh**.
* Event days therefore showed roughly **203 kWh higher average consumption** than non-event days.
* **Zone Z5** had the highest average electricity consumption at approximately **2577.46 kWh**.
* Temperature showed a positive correlation of approximately **0.274** with electricity consumption.
* Special events showed a positive correlation of approximately **0.203** with electricity consumption.
* Humidity had a weaker positive correlation of approximately **0.100** with electricity consumption.

These results suggest that city zone, weather conditions, and special events can contribute to variations in electricity demand.

---

## 💻 Interactive Prediction System

The project includes a console-based interface where users can enter:

* Zone number
* Tomorrow's temperature
* Tomorrow's humidity
* Special-event indicator (0/1)

The trained model then predicts the next day's electricity consumption.

Input validation is included to handle invalid zone numbers, temperature values, humidity percentages, event indicators, and non-numeric inputs.

---

## 📁 Project Structure

```text
city-energy-consumption-prediction/
│
├── City_Energy_Consumption_Project.ipynb
├── city_energy_data.csv
├── energy_prediction.py
└── README.md
```

---

## ▶️ How to Run the Project

1. Clone or download this repository.
2. Open `City_Energy_Consumption_Project.ipynb` in Google Colab or Jupyter Notebook.
3. Run the notebook cells from top to bottom.
4. View the analysis and visualizations.
5. Run the prediction section.
6. Enter the requested values to generate a next-day electricity consumption prediction.

---

## 🚀 Future Improvements

The project can be further improved by:

* Comparing Linear Regression with Random Forest and other regression models.
* Adding more historical electricity data.
* Including additional weather and calendar features.
* Developing a web-based prediction interface.
* Using real-world electricity consumption datasets.

---

## 👩‍💻 Author

**Neha Somwanshi**

Data Science Internship Project
