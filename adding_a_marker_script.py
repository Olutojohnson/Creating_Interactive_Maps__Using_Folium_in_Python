import folium
import webbrowser

# Create a map centered on Lagos, Nigeria
map_lagos = folium.Map(location=[6.5244, 3.3792], zoom_start=12)

# Add a marker for the National Museum Lagos
folium.Marker([6.4483, 3.4001], popup="National Museum Lagos").add_to(map_lagos)

# Save the map
map_lagos.save("map_with_marker.html")

# Automatically open the map in the default web browser
webbrowser.open("map_with_marker.html")
