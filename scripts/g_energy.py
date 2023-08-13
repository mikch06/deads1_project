import pandas as pd
# datainfo
# stations_XY_count : Anzahl Ladestationen pro Kanton.
# locations_XY_count : Anzahl Standorte pro Kanton.

def gold_energy():
    # Stromprudktion
    df = pd.read_csv("../data/silver/s_stromprduktion.csv")
    df.to_csv("../data/gold/g_stromproduktion.csv", index=False)

    # Landesverbrauch estimated!
    df1 = pd.read_csv("../data/silver/s_landesverbrauch-estimated.csv")
    df1.to_csv("../data/gold/g_landesverbrauch-estimated.csv", index=False)

    # Landesverbrauch / Endverbrauch
    df2 = pd.read_csv("../data/silver/s_landesverbrauch-endverbrauch.csv")
    df2.to_csv("../data/gold/g_landesverbrauch-endverbrauch.csv", index=False)