import pandas as pd
df = pd.read_json("../data/landing/data.ch.bfe.ladestellen-elektromobilitaet.json")
print(df.shape)
print(df.tail)
df = pd.read_json("../data/landing/status.ch.bfe.ladestellen-elektromobilitaet.json")
print(df.shape)
print(df.tail)
df = pd.read_csv("../data/landing/ich_tanke_strom_monthly.csv")
print(df.shape)
print(df.tail)


