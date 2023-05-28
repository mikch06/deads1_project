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





#df2 = pd.read_csv("../raw/csv/kantonsratswahl-2022-gde-risch.csv")
# profile = df.profile_report(html={'style':{'full_width':True}})
# profile.to_file(output_file="sgv-profile.html")
print(df.tail)
print(df.head(n=5))

visual = df.to_html("foo.html")
print(visual)
