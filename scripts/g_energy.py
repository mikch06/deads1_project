import pandas as pd
# datainfo
# stations_XY_count : Anzahl Ladestationen pro Kanton.
# locations_XY_count : Anzahl Standorte pro Kanton.

def gold_energy():
    df = pd.read_csv("../data/silver/s_stromprduktion.csv")


    df.to_csv("../data/gold/g_stromproduktion.csv", index=False)


    df1 = pd.read_csv("../data/silver/s_landesverbrauch-estimated.csv")

    df1.to_csv("../data/gold/g_landesverbrauch-estimated.csv", index=False)