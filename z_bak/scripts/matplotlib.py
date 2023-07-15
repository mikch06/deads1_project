import pandas as pd
import matplotlib.pyplot as plt

# prepare some data
# x = [1, 2, 3, 4, 5]
# y = [6, 7, 2, 4, 5]
# create a new plot with a title and axis labels
# f = figure(title="Bokeh Simple line example", x_axis_label='x', y_axis_label='y')
# # add a line renderer with legend and line thickness to the plot
# f.line(x, y, line_width=2)
# show(f)

# Simple line example (2) pandas
df = pd.read_csv("../data/bronze/bak/b_ich_tanke_strom_monthly.csv")
#lines = df.plot.line(title="Simple line example2")

##
# Funktionierender multiline plot

plt.rcParams["figure.figsize"] = [15, 15]
plt.rcParams["figure.autolayout"] = True
df = pd.read_csv("../data/bronze/bak/b_ich_tanke_strom_monthly.csv")
df.plot(title="Simple line example")
plt.show()




## Bokeh
# Bokeh Versuch
#df = pd.read_csv("../data/bronze/b_ich_tanke_strom_monthly.csv")
#p = figure(title="Bokeh multiline example", x_axis_label='Zeit', y_axis_label='Anzahl')
#source = ColumnDataSource(df)
#print(df.head())
#x = df['year']
#y = df['month']

#p.line(x, y, line_width=5)

#output_file("html/foo.html")
#source = ColumnDataSource(df)
#p = figure(x_axis_label='Zeit', y_axis_label='Anzahl', source=source)
#p = figure()
#p.line(x='stations_TG_count', y='stations_ZH_count', source=source)
#show(p)

