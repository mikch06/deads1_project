from bokeh.plotting import figure, show, ColumnDataSource, output_file
from bokeh.models import HoverTool
from bokeh.palettes import Category10
import pandas as pd

df = pd.read_csv("../data/bronze/b_ich_tanke_strom_monthly.csv")
print(df.head())

# Datetime of two columns
# https://sparkbyexamples.com/pandas/pandas-convert-multiple-columns-to-datetime-type/
df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))
df = df.filter(regex="(date|stations_)")

columns = df.filter(regex="(stations_)")

output_file("html/v_charging_stations.html")
source = ColumnDataSource(df)
#p = figure(x_axis_label='Zeit', y_axis_label='Anzahl', source=source)
p = figure(title="Ladestationen in den Kantonen", x_axis_label='Zeit', y_axis_label='Anzahl', x_axis_type='datetime',
frame_width=800, frame_height=300)

for i in columns:
    p.line(x='date', y=i, source=source, line_width=1)
    # p.line(x='date', y='stations_ZG_count', source=source)
    print("Stations for line graph: ", i)
show(p)
