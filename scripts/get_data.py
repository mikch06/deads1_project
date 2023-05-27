import requests


# Statische Informationen der Ladestationen (EVSEData) - kontinuierlich aktualisiert
# https://opendata.swiss/dataset/ladestationen-fuer-elektroautos
# https://opendata.swiss/dataset/ladestationen-fuer-elektroautos/resource/e33957be-180a-422b-90a5-fbfe9774927a
def data_charginstation_data():
    url = "https://data.geo.admin.ch/ch.bfe.ladestellen-elektromobilitaet/data/oicp/ch.bfe.ladestellen-elektromobilitaet.json"
    r = requests.get(url)
    with open("../data/landing/data.ch.bfe.ladestellen-elektromobilitaet.json", "w") as file:
        file.write(str(r.content))

# Verfügbarkeits-Informationen der Ladestationen (EVSEStatus) - kontinuierlich aktualisiert
# https://opendata.swiss/dataset/ladestationen-fuer-elektroautos
# https://opendata.swiss/dataset/ladestationen-fuer-elektroautos/resource/4d467a51-0bc9-48ce-aa2a-3d3bcaa7e7e9
def data_charginstation_avail():
    url = "https://data.geo.admin.ch/ch.bfe.ladestellen-elektromobilitaet/status/oicp/ch.bfe.ladestellen-elektromobilitaet.json"
    r = requests.get(url)
    with open("../data/landing/status.ch.bfe.ladestellen-elektromobilitaet.json", 'w') as file:
        file.write(str(r.content))
def data_tanke_strom_monthly():
    url = "https://www.uvek-gis.admin.ch/BFE/ogd/57/ich_tanke_strom_Kennzahlen_monatlich.csv"
    r = requests.get(url)
    with open("../data/monthly.csv", "w") as file:
        file.write(str(r.content))


data_charginstation_data()
data_charginstation_avail()
data_tanke_strom_monthly()