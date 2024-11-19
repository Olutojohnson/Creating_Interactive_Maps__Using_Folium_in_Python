import folium
import webbrowser

# Create a map centered on Lagos, Nigeria
map_lagos = folium.Map(location=[6.5244, 3.3792], zoom_start=12)

# Add a circle for the Lekki Conservation Center
folium.Circle(
    location=[6.4463, 3.5312],
    radius=500,  # Radius in meters
    popup="Lekki Conservation Center",
    color="green",
    fill=True,
    fill_opacity=0.5
).add_to(map_lagos)

# Save the map
map_lagos.save("map_with_circle.html")

# Automatically open the map in the default web browser
webbrowser.open("map_with_circle.html")
