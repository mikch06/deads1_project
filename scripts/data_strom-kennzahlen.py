import pandas as pd

df = pd.read_csv("https://www.uvek-gis.admin.ch/BFE/ogd/57/ich_tanke_strom_Kennzahlen_monatlich.csv")

print(df.columns)
print(df.head(n=5))

