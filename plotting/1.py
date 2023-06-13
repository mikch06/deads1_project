from bokeh.plotting import figure, show, ColumnDataSource
import pandas as pd
import matplotlib.pyplot as plt

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]


# create a new plot with a title and axis labels
p = figure(title="Simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness to the plot
p.line(x, y, line_width=2)

show(p)



# Simple line example (2) pandas
df = pd.read_csv("../data/bronze/b_ich_tanke_strom_monthly.csv")
lines = df.plot.line(title="Simple line example2")



## Bokeh
# Bokeh Versuch
df = pd.read_csv("../data/bronze/b_ich_tanke_strom_monthly.csv")
print(df.head())
source = ColumnDataSource(df)
f = figure(title="Bokeh")
show(f)

##
# Funktionierender multiline plot

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

df = pd.read_csv("../data/bronze/b_ich_tanke_strom_monthly.csv")
df.plot(title="Simple line example")

plt.show()
