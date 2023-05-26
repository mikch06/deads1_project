import pandas as pd
import ydata_profiling

df = pd.read_csv("../raw/csv/kantonsratswahl-2022-gde-risch.csv")

#df2 = pd.read_csv("../raw/csv/kantonsratswahl-2022-gde-risch.csv")
# profile = df.profile_report(html={'style':{'full_width':True}})
# profile.to_file(output_file="sgv-profile.html")
print(df.shape)
print(df.head(n=5))

visual = df.to_html("foo.html")
print(visual)
