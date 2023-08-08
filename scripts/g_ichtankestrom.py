import pandas as pd
# datainfo
# stations_XY_count : Anzahl Ladestationen pro Kanton.
# locations_XY_count : Anzahl Standorte pro Kanton.

def gold_ichtankestrom():
    df = pd.read_csv("../data/silver/s_ich_tanke_strom_monthly.csv")

    df1 = df.filter(regex="(year|month|locations_|stations_)")
    # Cut out locations and station all over CH
    del df1["locations_CH_count"]
    del df1["stations_CH_count"]
    df1.to_csv("../data/gold/g_ich_tanke_strom_monthly.csv", index=False)

    # Sum CH locations
    df2 = df[["month", "year", "locations_CH_count"]]
    df2.to_csv("../data/gold/g_ich_tanke_strom_monthly_locations_CH.csv")

    # Sum CH stations
    df3 = df[["month", "year", "stations_CH_count"]]
    df3.to_csv("../data/gold/g_ich_tanke_strom_monthly_stations_CH.csv")
