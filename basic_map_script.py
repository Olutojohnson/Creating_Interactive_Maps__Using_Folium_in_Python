import folium
import webbrowser

# Create a basic map centered on Lagos, Nigeria
map_lagos = folium.Map(location=[6.5244, 3.3792], zoom_start=12)
folium.TileLayer('OpenStreetMap', name='Default').add_to(map_lagos)

# Save the map to an HTML file
map_lagos.save("basic_map.html")

# Automatically open the map in the default web browser
webbrowser.open("basic_map.html")

