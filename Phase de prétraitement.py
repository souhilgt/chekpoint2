
import pandas as pd

data = pd.read_csv("titanic-passengers.csv", delimiter=";")


print(data.head())

print(data.info())



data['Age'].fillna(data['Age'].median(), inplace=True)
data['Fare'].fillna(data['Fare'].median(), inplace=True)


data['Cabin'].fillna("Unknown", inplace=True)


most_common_embarked = data['Embarked'].mode()[0]
data['Embarked'].fillna(most_common_embarked, inplace=True)


print(data.isnull().sum())



