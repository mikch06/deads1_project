import random

from bokeh.plotting import figure, show, ColumnDataSource, output_file
from bokeh.models import HoverTool
from bokeh.palettes import Viridis256
import collections
import pandas as pd




def visualize_ichtankestrom():
    df = pd.read_csv("../data/gold/g_ich_tanke_strom_monthly.csv")
    print(df.head())

    # Datetime of two columns
    # https://sparkbyexamples.com/pandas/pandas-convert-multiple-columns-to-datetime-type/
    df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))
    df = df.filter(regex="(date|stations_)")

    stations = df.filter(regex="(stations_)")
    # locations = df.filter(regex="(locations:)")



    output_file("/var/www/deads/html/plots/v_charging_stations.html")
    source = ColumnDataSource(df)
    p = figure(title="Ladestationen in allen Kantonen", x_axis_label='Zeit', y_axis_label='Anzahl', x_axis_type='datetime',
    frame_width=1200, frame_height=800)

    for i in stations:
        # graph color random from bokeh palettes
        colors = random.choice(Viridis256)

        p.line(x='date', y=i, source=source, line_width=2, legend_label=i, color=colors)
        p.legend.title = 'Kantone'
        p.legend.location = "bottom_left"
        print(colors)

    # Hover Tooltips in graph
    hover = HoverTool(tooltips =[
         ('Datum','$x'),('Anzahl', '$y{(0)}')])
    p.add_tools(hover)
    show(p)
