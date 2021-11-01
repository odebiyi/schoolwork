import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv(r"C:\Users\Ayodeji.odebiyi.GLOBALACCELEREX\Desktop\LECTURES\DATA MINING\PRAC 5\specs\marks_question1.csv")
print(df)

df.shape
df.head()
df.describe()
df.plot.scatter(x= 'midterm', y= 'final')
plt.title('Linear Graph')
plt.xlabel('Midterm')
plt.ylabel('final')
plt.show()
