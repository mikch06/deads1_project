from bokeh.plotting import figure, show, ColumnDataSource
import pandas as pd

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]


# create a new plot with a title and axis labels
p = figure(title="Simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness to the plot
p.line(x, y, line_width=2)

show(p)


df = pd.read_csv("../data/landing/ich_tanke_strom_monthly.csv")
#df = df.filter(regex="(year|month|locations_|stations_)")
group = df.groupby(('locations_AG_count', 'locations_AI_count'))
source = ColumnDataSource(group)
p = figure(title="Stromtanken samples", x_axis_label='x', y_axis_label='y')
p.line(y="year", source=source)
show(p)

