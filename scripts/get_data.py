import requests


# Statische Informationen der Ladestationen (EVSEData) - kontinuierlich aktualisiert
# https://opendata.swiss/dataset/ladestationen-fuer-elektroautos
# https://opendata.swiss/dataset/ladestationen-fuer-elektroautos/resource/e33957be-180a-422b-90a5-fbfe9774927a
def data_charginstation_data():
    url = "https://data.geo.admin.ch/ch.bfe.ladestellen-elektromobilitaet/data/oicp/ch.bfe.ladestellen-elektromobilitaet.json"
    r = requests.get(url)
    with open("../data/landing/data.ch.bfe.ladestellen-elektromobilitaet.json", "wb") as file:
        file.write(r.content)


# Verfügbarkeits-Informationen der Ladestationen (EVSEStatus) - kontinuierlich aktualisiert
# https://opendata.swiss/dataset/ladestationen-fuer-elektroautos
# https://opendata.swiss/dataset/ladestationen-fuer-elektroautos/resource/4d467a51-0bc9-48ce-aa2a-3d3bcaa7e7e9
def data_charginstation_avail():
    url = "https://data.geo.admin.ch/ch.bfe.ladestellen-elektromobilitaet/status/oicp/ch.bfe.ladestellen-elektromobilitaet.json"
    r = requests.get(url)
    with open("../data/landing/status.ch.bfe.ladestellen-elektromobilitaet.json", "wb") as file:
        file.write(r.content)


def data_tanke_strom_monthly():
    url = "https://www.uvek-gis.admin.ch/BFE/ogd/57/ich_tanke_strom_Kennzahlen_monatlich.csv"
    r = requests.get(url)
    with open("../data/landing/ich_tanke_strom_monthly.csv", "wb") as file:
        file.write(r.content)


# Landesverbrauch und Endverbrauch
# https://opendata.swiss/de/dataset/energiedashboard-ch-stromverbrauch-swissgrid/resource/3569b65f-1afc-4541-876f-cd98f9256cb1
def data_lverbrauch_everbrauch():
    url = "https://bfe-energy-dashboard-ogd.s3.amazonaws.com/ogd103_stromverbrauch_swissgrid_lv_und_endv.csv"
    r = requests.get(url)
    with open("../data/landing/landesverbrauch-endverbrauch.csv", "wb") as file:
        file.write(r.content)

# Stromproduktion
# https://opendata.swiss/de/dataset/energiedashboard-ch-stromproduktion-swissgrid/resource/619e6fa0-7c2b-46dd-9633-7bd60fc5ec16
def data_stromproduktion():
    url = "https://bfe-energy-dashboard-ogd.s3.amazonaws.com/ogd104_stromproduktion_swissgrid.csv"
    r = requests.get(url)
    with open("../data/landing/stromproduktion.csv", "wb") as file:
        file.write(r.content)



data_charginstation_data()
data_charginstation_avail()
data_tanke_strom_monthly()
data_lverbrauch_everbrauch()
data_stromproduktion()