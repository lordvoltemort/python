import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_changer(elev):
    if elev<1000:
        return 'green'
    elif 1000 <= elev < 3000 :
        return 'blue'
    else :
        return 'red'

map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")
for lt,ln,el in zip(lat,lon,elev):
    #fg.add_child(folium.Marker(location=[38.2,-99.1],popup="Hi I am marker",icon=folium.Icon(color='green')))
    fg.add_child(folium.Marker(location=[lt,ln],popup=str(el)+" m",icon=folium.Icon(color=color_changer(el))))
map.add_child(fg)

map.save("map2.html")
