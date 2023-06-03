import pandas as pd
# datainfo
# stations_XY_count : Anzahl Ladestationen pro Kanton.
# locations_XY_count : Anzahl Standorte pro Kanton.

df = pd.read_csv("../data/landing/ich_tanke_strom_monthly.csv")

df1 = df.filter(regex="(year|month|locations_|stations_)")
# pd.set_option("display.max_rows", None)
# pd.set_option('display.max_columns', None)

df2 = df.filter(regex="(year|month|stations_)")
pd.set_option("display.max_rows", None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 100)
print(df1)
#print(df2)


df1.to_csv("../data/bronze/b_ich_tanke_strom_monthly.csv", index=False)


