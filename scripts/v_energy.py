import random

from bokeh.plotting import figure, show, ColumnDataSource, output_file
from bokeh.models import HoverTool
from bokeh.palettes import Viridis256
import pandas as pd

def visualize_energy():
    # Stromproduktion
    df = pd.read_csv("../data/gold/g_stromproduktion.csv")
    df = df.iloc[::-1]
    df.to_html('/var/www/deads/html/plots/v_stromproduktion.html', index=False, border=0, col_space="100", justify='left', classes='')

    # Landesverbrauch (estimated)
    df1 = pd.read_csv("../data/gold/g_landesverbrauch-estimated.csv")
    df1 = df1.iloc[::-1]
    df1.to_html('/var/www/deads/html/plots/v_landesverbrauch-estimated.html', index=False, border=0, col_space="100", justify='left', classes='')

    # Landesverbrauch effektiv
    df2 = pd.read_csv("../data/gold/g_landesverbrauch-endverbrauch.csv")
    df2 = df2.iloc[::-1]
    df2.to_html('/var/www/deads/html/plots/v_landesverbrauch-endverbrauch.html', index=False, border=0, col_space="100", justify='left', classes='')