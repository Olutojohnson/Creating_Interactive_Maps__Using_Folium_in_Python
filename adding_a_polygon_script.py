import folium
import webbrowser

# Create a map centered on Lagos, Nigeria
map_lagos = folium.Map(location=[6.5244, 3.3792], zoom_start=12)

# Define the coordinates of Victoria Island
victoria_island_coords = [
    [6.4281, 3.4215],
    [6.4226, 3.4394],
    [6.4309, 3.4476],
    [6.4426, 3.4282]
]

# Add a polygon for Victoria Island
folium.Polygon(
    locations=victoria_island_coords,
    popup="Victoria Island",
    color="blue",
    fill=True,
    fill_opacity=0.5
).add_to(map_lagos)

# Save the map
map_lagos.save("map_with_polygon.html")

# Automatically open the map in the default web browser
webbrowser.open("map_with_polygon.html")
