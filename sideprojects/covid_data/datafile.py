import pandas
import folium

#importera karta
#fixa relevant data i listor
#lägga till element på kartan
#visualisera m.h.a färger

df = pandas.read_csv("covid_data.csv")

lat = list(df["Latitude"])
lon = list(df["Longitude"])
confirmed = list(df["Confirmed"])
deaths = list(df["Deaths"])

map = folium.Map(location = [60.1733244, 24.9410248], zoom_start = 12, tiles = "Stamen Terrain")

fgconfirmed = folium.FeatureGroup(name = "Confirmed Cases")
fgdeaths = folium.FeatureGroup(name = "Total Deaths")

#Adding balls to correspond against coordinates

def opacity_picker (num):
    if num < 5000: return 0.1
    elif num >= 5000 and num < 15000: return 0.3
    elif num >= 15000 and num < 50000: return 0.5
    elif num >= 50000 and num < 250000: return 0.7
    else: return 0.9
def radius_picker (num):
    return num/50000


for lt, ln, conf, deaths in zip(lat, lon, confirmed, deaths):

    fgconfirmed.add_child(folium.CircleMarker(location = [lt,ln], radius = radius_picker(conf)*2, popup = "Confirmed: " + str(conf), color = "orange", fill_color = "orange"))

    fgdeaths.add_child(folium.CircleMarker(location = [lt,ln], radius = radius_picker(deaths)*10, popup = "Deaths: " + str(deaths), color = "red", fill_color = "red"))

map.add_child(fgconfirmed)
map.add_child(fgdeaths)
map.add_child(folium.LayerControl())

map.save("Covidmap.html")