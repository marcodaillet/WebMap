import folium
import pandas

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

### Volcanoes

def color_producer(elevation):
	if elevation <= 1500:
		return 'green'
	elif 1500 <= elevation <= 3000:
		return 'orange'
	else:
		return 'red'

data = pandas.read_csv("Volcanoes.txt")

latitude = list(data["LAT"])
longitude = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
info = []

for na, el in zip(name, elev):
	i = na + "\n----\n" + str(el) + " meters"	
	info.append(i)
	
fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, inf, el in zip(latitude , longitude, info, elev):
	fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=inf, fill_color=color_producer(el), color ='grey', fill_opacity=0.5))



### Population
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 50000000 else 'orange' if  50000001 <= x['properties']['POP2005'] < 100000000 else 'red'}))



map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")