import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json("data/json/kantonsratswahl-2022-gde-risch.json")

#print(df)

df = pd.read_csv("data/csv/kantonsratswahl-2022-gde-risch.csv")

#print(df)


plot_frame = pd.read_csv("data/csv/kantonsratswahl-2022-gde-risch.csv", index_col=1, parse_dates=True)

plot_frame.head()
print(plot_frame)


plot_frame.plot()
plt.show()











