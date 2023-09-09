
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Chargez leS données
data = pd.read_csv('titanic-passengers.csv', sep=';')


print(data.head(100))
print(data.info(100))




plt.figure(figsize=(8, 6))
sns.histplot(data['Age'].dropna(), bins=20, kde=True)
plt.title('Distribution de l\'âge')
plt.xlabel('Âge')
plt.ylabel('Nombre d\'individus')



plt.figure(figsize=(8, 6))
sns.boxplot(x='Sex', y='Age', data=data)
plt.title('Corrélation entre le sexe et l\'âge')
plt.xlabel('Sexe')
plt.ylabel('Âge')
plt.show()