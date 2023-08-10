import random

from bokeh.plotting import figure, show, ColumnDataSource, output_file
from bokeh.models import HoverTool
from bokeh.palettes import Viridis256
import pandas as pd

def visualize_energy():
    df = pd.read_csv("../data/gold/g_stromproduktion.csv")
    html = df.to_html(border=1)
    print("HTML Output:", html)

    output_html = open("/var/www/deads/html/plots/v_stromproduktion.html", "w")
    output_html.write(html)
    output_html.close()