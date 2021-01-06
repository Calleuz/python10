import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])



map = folium.Map(location = [48, -120], zoom_start = 12, tiles = "Stamen Terrain")

fgVolcanoes = folium.FeatureGroup(name = "Volcanoes")
fgPopulation = folium.FeatureGroup(name = "Population")


for lt, ln, name, elev in zip(lat,lon, name, elev):
    if elev > 1500 and elev < 3000:
        col = "green"
    elif elev > 3000: col = "black"
    else: col = "lightgreen"
    fgVolcanoes.add_child(folium.Marker(location = [lt,ln], radius = 1, popup = name + ", Altitude: "+ str(elev) + "m.", icon = folium.Icon(color = col, icon = 'default')))
#Creating polygons that display countries
fgPopulation.add_child(folium.GeoJson(data =(open("world.json", "r", encoding = "utf-8-sig").read()), style_function = lambda x: {"fillColor": "Red" if x['properties']['POP2005'] > 50000000 else "Yellow" if x['properties']['POP2005'] < 50000000 and x['properties']['POP2005'] > 1000000 else 'Green'}))

map.add_child(fgVolcanoes)
map.add_child(fgPopulation)
map.add_child(folium.LayerControl())
map.save("mymap.html")