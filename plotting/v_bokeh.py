from bokeh.plotting import figure, show, ColumnDataSource, output_file
from bokeh.models import HoverTool
from bokeh.palettes import Category10
import pandas as pd

## Bokeh
# Bokeh Versuch
df = pd.read_csv("../data/bronze/b_ich_tanke_strom_monthly.csv")
#p = figure(title="Bokeh multiline example", x_axis_label='Zeit', y_axis_label='Anzahl')
#source = ColumnDataSource(df)
print(df.head())


# Datetime of two columns
# https://sparkbyexamples.com/pandas/pandas-convert-multiple-columns-to-datetime-type/
df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))
df = df.filter(regex="(date|stations_)")

columns = df.filter(regex="(stations_)")


print(df.head())


#p.line(x, y, line_width=5)

#output_file("html/foo.html")
source = ColumnDataSource(df)
#p = figure(x_axis_label='Zeit', y_axis_label='Anzahl', source=source)
p = figure(title="Ladestationen in den Kantonen", x_axis_label='Zeit', y_axis_label='Anzahl', x_axis_type='datetime')
p.line(x='date', y='stations_ZH_count', source=source)
p.line(x='date', y='stations_ZG_count', source=source)


show(p)

