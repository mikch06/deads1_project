import random
from bokeh.plotting import figure, show, ColumnDataSource, output_file
from bokeh.models import HoverTool
from bokeh.palettes import Viridis256
import pandas as pd
def visualize_ichtankestrom():
    global i
    df = pd.read_csv("../data/gold/g_ich_tanke_strom_monthly.csv")
    print(df.head())

    # Datetime of two columns
    # https://sparkbyexamples.com/pandas/pandas-convert-multiple-columns-to-datetime-type/
    df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))
    df = df.filter(regex="(date|stations_)")

    stations = df.filter(regex="(stations_)")
    # locations = df.filter(regex="(locations:)")

    output_file("/var/www/deads/html/plots/v_charging_stations.html", title="Ladestationen in allen Kantonen")
    source = ColumnDataSource(df)
    p = figure(title="Ladestationen in allen Kantonen", x_axis_label='Zeit', y_axis_label='Anzahl',
               x_axis_type='datetime',
               frame_width=1200, frame_height=800)

    for i in stations:
        # Graph color random from bokeh palettes
        colors = random.choice(Viridis256)

        p.line(x='date', y=i, source=source, line_width=2, legend_label=i, color=colors)
        p.legend.title = 'Kantone'
        p.legend.location = "bottom_left"
        p.toolbar.autohide = True

        # Hover Tooltips in graph
        hover = HoverTool(tooltips=[
            # ('Datum', '$x'),
            ('Anzahl', '$y{(0)}')])
        # ('Kanton', i)])
    p.add_tools(hover)
    show(p)

def visualize_ichtankestrom_CH():
    # Ldestationen Locations
    df = pd.read_csv("../data/gold/g_ich_tanke_strom_monthly_locations_CH.csv")
    # Inverse data publishing
    df = df.iloc[::-1]
    df.to_html("/var/www/deads/html/plots/v_charging_locations_CH.html", index=False, border=0, justify='left', classes='')

    # Ladestationen Stations
    df1 = pd.read_csv("../data/gold/g_ich_tanke_strom_monthly_stations_CH.csv")
    # Inverse data publishing
    df1 = df1.iloc[::-1]
    df1.to_html("/var/www/deads/html/plots/v_charging_stations_CH.html", index=False, border=0, justify='left', classes='')




