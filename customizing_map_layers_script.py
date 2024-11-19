import folium
import webbrowser

# Create a map centered on Lagos, Nigeria
map_lagos = folium.Map(location=[6.5244, 3.3792], zoom_start=12, name='OpenStreetMap')

# Add ESRI World Terrain tile layer with attribution
folium.TileLayer(
       name="Esri World Terrain",
       tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer/tile/{z}/{y}/{x}',
       attr='Tiles &copy; Esri &mdash; Source: USGS, Esri, TANA, DeLorme, and NPS').add_to(map_lagos)

# Add ESRI World Imagery tile layer with attribution
folium.TileLayer(
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    name="ESRI World Imagery",
    attr='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
).add_to(map_lagos)

# Add ESRI World Topo tile layer with attribution
folium.TileLayer(
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}',
    name="ESRI World Topo",
    attr='Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ, TomTom, Intermap, iPC, USGS, FAO, NPS, NRCAN, GeoBase, Kadaster NL, Ordnance Survey, Esri Japan, METI, Esri China (Hong Kong), and the GIS User Community'
).add_to(map_lagos)

# Add Layer Control
folium.LayerControl().add_to(map_lagos)

# Save the map to an HTML file
map_lagos.save("map_with_layers.html")

# Open the saved map in a web browser
webbrowser.open("map_with_layers.html")
