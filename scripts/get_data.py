import requests


def tanke_strom_monthly():
    print("Download monthly data")
    url = "https://www.uvek-gis.admin.ch/BFE/ogd/57/ich_tanke_strom_Kennzahlen_monatlich.csv"
    r = requests.get(url)
    with open("../data/monthly.json", 'wb') as file:
        file.write(r.content)
#df = pd.read_csv("https://www.uvek-gis.admin.ch/BFE/ogd/57/ich_tanke_strom_Kennzahlen_monatlich.csv")



