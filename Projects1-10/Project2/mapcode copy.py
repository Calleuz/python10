import folium

#Adding a starting point
map = folium.Map(location = [60.1733244,24.9410248], tiles = "Stamen Terrain")
#Adding a point on the map with information
#map.add_child(folium.Marker(location = [60.1733244,24.9410248], popup = "Lorem", icon = folium.Icon(color = "green")))


#Adding a feature-group
fg = folium.FeatureGroup(name = "newmap")

elements = {"M1":[60.1733244,24.9410248], "M2": [60.9533244,24.9410248], "M3": [60.0133244,24.9410248]}

for key in elements:
    fg.add_child(folium.Marker(location = elements[key], popup = key, icon = folium.Icon(color = "green")))

map.add_child(fg)
map.save("mymap.html")