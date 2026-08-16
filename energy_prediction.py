
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


# ---------------------------------
# 1. Load Dataset
# ---------------------------------

df = pd.read_csv("city_energy_data.csv")

print("Dataset loaded successfully.")
print("Dataset Shape:", df.shape)


# ---------------------------------
# 2. Data Cleaning
# ---------------------------------

df["Date"] = pd.to_datetime(df["Date"])

df = df.drop_duplicates()

print("\nMissing Values:")
print(df.isnull().sum())


# ---------------------------------
# 3. Create Zone Number
# ---------------------------------

df["ZoneNumber"] = (
    df["ZoneID"]
    .str.replace("Z", "", regex=False)
    .astype(int)
)


# ---------------------------------
# 4. Sort Data
# ---------------------------------

df = df.sort_values(
    ["ZoneID", "Date"]
)


# ---------------------------------
# 5. Create Next-Day Features
# ---------------------------------

df["NextTemp"] = (
    df.groupby("ZoneID")["AvgTemperature"]
    .shift(-1)
)

df["NextHumidity"] = (
    df.groupby("ZoneID")["Humidity"]
    .shift(-1)
)

df["NextEvent"] = (
    df.groupby("ZoneID")["SpecialEvent"]
    .shift(-1)
)

df["NextDayEnergy"] = (
    df.groupby("ZoneID")["EnergyConsumption"]
    .shift(-1)
)


# Remove rows where next-day information is unavailable

df_model = df.dropna(
    subset=[
        "NextTemp",
        "NextHumidity",
        "NextEvent",
        "NextDayEnergy"
    ]
).copy()


# ---------------------------------
# 6. Select Features and Target
# ---------------------------------

X = df_model[
    [
        "ZoneNumber",
        "NextTemp",
        "NextHumidity",
        "NextEvent"
    ]
]

y = df_model["NextDayEnergy"]


# ---------------------------------
# 7. Train-Test Split
# ---------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# ---------------------------------
# 8. Train Linear Regression Model
# ---------------------------------

model = LinearRegression()

model.fit(
    X_train,
    y_train
)

print("\nModel trained successfully.")


# ---------------------------------
# 9. Model Evaluation
# ---------------------------------

y_pred = model.predict(X_test)

mae = mean_absolute_error(
    y_test,
    y_pred
)

print(
    "Mean Absolute Error:",
    round(mae, 2),
    "kWh"
)


# ---------------------------------
# 10. Interactive Prediction
# ---------------------------------

def predict_energy():

    try:

        print(
            "\n--- City Energy Consumption Predictor ---"
        )

        zone = int(
            input("Enter Zone Number (1-5): ")
        )

        temperature = float(
            input(
                "Enter tomorrow's temperature (°C): "
            )
        )

        humidity = float(
            input(
                "Enter tomorrow's humidity (%): "
            )
        )

        event = int(
            input(
                "Special Event tomorrow? "
                "(0 = No, 1 = Yes): "
            )
        )


        # -----------------------------
        # Input Validation
        # -----------------------------

        if zone < 1 or zone > 5:

            print(
                "Invalid Zone! "
                "Enter a number between 1 and 5."
            )

            return


        if temperature < -10 or temperature > 55:

            print(
                "Invalid Temperature! "
                "Enter a realistic temperature."
            )

            return


        if humidity < 0 or humidity > 100:

            print(
                "Invalid Humidity! "
                "Enter a value between 0 and 100."
            )

            return


        if event not in [0, 1]:

            print(
                "Invalid Event! "
                "Enter only 0 or 1."
            )

            return


        # -----------------------------
        # Prepare User Input
        # -----------------------------

        user_data = pd.DataFrame({

            "ZoneNumber": [zone],

            "NextTemp": [temperature],

            "NextHumidity": [humidity],

            "NextEvent": [event]

        })


        # -----------------------------
        # Prediction
        # -----------------------------

        prediction = model.predict(
            user_data
        )


        print(
            "\nPredicted Tomorrow's "
            "Energy Consumption:",
            round(prediction[0], 2),
            "kWh"
        )


    except ValueError:

        print(
            "\nInvalid input! "
            "Please enter numeric values only."
        )


# ---------------------------------
# 11. Run Prediction System
# ---------------------------------

if __name__ == "__main__":

    predict_energy()
