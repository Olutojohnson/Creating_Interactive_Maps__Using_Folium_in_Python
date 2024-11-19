import folium
import webbrowser

# Create a map centered on Lagos, Nigeria
map_lagos = folium.Map(location=[6.5244, 3.3792], zoom_start=12)

# Example GeoJSON data (simple rectangle in Lagos)
geojson_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [3.35, 6.5],
                    [3.42, 6.5],
                    [3.42, 6.55],
                    [3.35, 6.55],
                    [3.35, 6.5]
                ]]
            },
            "properties": {
                "name": "Sample Area"
            }
        }
    ]
}

# Add GeoJSON data to the map
folium.GeoJson(geojson_data, name="Sample GeoJSON").add_to(map_lagos)

# Save the map
map_lagos.save("map_with_geojson.html")

# Automatically open the map in the default web browser
webbrowser.open("map_with_geojson.html")
