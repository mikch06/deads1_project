import pandas as pd
# datainfo
# stations_XY_count : Anzahl Ladestationen pro Kanton.
# locations_XY_count : Anzahl Standorte pro Kanton.

def gold_ichtankestrom():
    df = pd.read_csv("../data/silver/s_ich_tanke_strom_monthly.csv")

    df1 = df.filter(regex="(year|month|locations_|stations_)")

    df1.to_csv("../data/gold/g_ich_tanke_strom_monthly.csv", index=False)

