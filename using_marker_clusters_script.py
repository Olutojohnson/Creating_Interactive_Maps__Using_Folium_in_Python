import folium
import webbrowser
from folium.plugins import MarkerCluster

# Create a map centered on Lagos, Nigeria
map_lagos = folium.Map(location=[6.5244, 3.3792], zoom_start=12)

# Create a marker cluster
marker_cluster = MarkerCluster().add_to(map_lagos)

# Add multiple markers to the cluster
locations = [[6.6018, 3.3515], [6.4281, 3.4215], [6.4463, 3.5312]]
for location in locations:
    folium.Marker(location, popup=f"Location: {location}").add_to(marker_cluster)

# Save the map
map_lagos.save("map_with_marker_cluster.html")

# Automatically open the map in the default web browser
webbrowser.open("map_with_marker_cluster.html")
