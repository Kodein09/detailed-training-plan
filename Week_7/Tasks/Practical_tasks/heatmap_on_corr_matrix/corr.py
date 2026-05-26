import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('iris')

corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Корреляционная матрица")
plt.grid()
plt.show()

for i in df.columns:
    print(i)

sns.boxplot(df, linewidth=3, linecolor='black', gap=2, x='species', y='petal_length')
plt.title("Boxplot of Leafs")
plt.legend(["Лепестки"])
plt.grid()
plt.show()

sns.violinplot(df, x='species', y='petal_length', linewidth=1, linecolor='black')
plt.legend(['Лепестки'])
plt.grid()
plt.show()

sns.pairplot(df)
plt.grid()
plt.show()