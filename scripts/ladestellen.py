import pandas as pd

df = pd.read_json("../ev/ch.bfe.ladestellen-elektromobilitaet.json")

print(df.shape)

print(df.head(n=5))
