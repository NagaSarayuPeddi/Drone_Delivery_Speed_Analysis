import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

file_path = "/content/drone_robot_delivery_dataset.csv"
df = pd.read_csv(file_path)
df['speed']=df['distance_km']/df['delivery_time_minutes']

print("Dataset Info:", df.info())
print("Dataset Shape:", df.shape)
print("\nColumns:\n", df.columns)
print(df.head())

dfNum = df.select_dtypes(include=[np.number]).dropna()

# Correlation matrix
print("\nCorrelation Matrix:\n")
print(dfNum.corr())
#print("\n with categorical data")
#print(df.corr())

dfNum.head()

Y=dfNum['speed']
X=dfNum.drop(dfNum.columns[0], axis=1).drop(dfNum.columns[5], axis=1).drop(dfNum.columns[3], axis=1)
#print(dfNum.columns[4])

model = LinearRegression()
model.fit(X_train, Y_train)
print("\nModel trained", model)
# Predictions
y_pred = model.predict(X_test)

r2 = r2_score(Y_test, y_pred)
mse = mean_squared_error(Y_test, y_pred)

print("\nModel Performance")
print("-----------------")
print("R-squared:", round(r2, 4))
print("MSE:", round(mse, 4))

print("\nCoefficients:")
print("\nIntercepts:")
print(round(model.intercept_,4), "\n")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {round(coef,4)}")

compare_df = pd.DataFrame({'Actual': Y_test, 'Predicted': y_pred})
print(compare_df.head(),"\n")
print(pd.Series(y_pred[:6], index=Y_test[:6].index))
print(pd.Series(Y_test[:6], index=Y_test[:6].index))
