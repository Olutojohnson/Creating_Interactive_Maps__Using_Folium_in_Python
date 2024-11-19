import folium
import webbrowser

# Create a map centered on Lagos, Nigeria
map_lagos = folium.Map(location=[6.5244, 3.3792], zoom_start=12)

# Define the line connecting Ikeja to Victoria Island
line_coords = [
    [6.6018, 3.3515],  # Ikeja
    [6.4281, 3.4215]   # Victoria Island
]

# Add a line to the map
folium.PolyLine(
    locations=line_coords,
    color="red",
    weight=3,
    opacity=0.7
).add_to(map_lagos)

# Save the map
map_lagos.save("map_with_line.html")

# Automatically open the map in the default web browser
webbrowser.open("map_with_line.html")
