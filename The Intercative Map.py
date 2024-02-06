#The visualization map code is as follows (first, install Flask and folium libraries. Then, create a Python file called app. py, containing the code. The purpose of the code is to simulate building data (longitude and latitude, building name, building rating), create maps, and create building markers. Next, create a folder called templates in the root directory of the project, and create an HTML file called index.xml in this folder. Enter the statement to create the webpage. Now, run the Python app. py to start the application and access it in the browser http://127.0.0.1:5000/ View interactive map)


from flask import Flask, render_template
import folium
from folium.plugins import MarkerCluster

app = Flask(__name__)

# Simulated building data, formatted as (latitude, longitude, building name, protection value score)
buildings_data = [
    (45.43417, 12.3389, "Venice St. Mark's Square", 8.654),

    # Add more building data
]

@app.route('/')
def index():
    # Create a map
    mymap = folium.Map(location=[buildings_data[0][0], buildings_data[0][1]], zoom_start=10)

    # Use the MarkerCluster plugin to create building markers
    marker_cluster = MarkerCluster().add_to(mymap)

    for building in buildings_data:
        folium.Marker(location=[building[0], building[1]], popup=f"{building[2]} - Protection Score: {building[3]}").add_to(marker_cluster)

    # Save the map as an HTML file
    mymap.save('templates/map.html')

    return render_template('index.html', buildings=buildings_data)

if __name__ == '__main__':
    app.run(debug=True)





Content in Hyml web pages
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buildings Map</title>
    <!-- Include Leaflet CSS file -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <!-- Include Leaflet JavaScript file -->
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
</head>
<body>
    <!-- Place map container here -->
    <div id="map" style="width: 100%; height: 600px;"></div>

    <script>
        var mymap = L.map('map').setView([{{ buildings[0][0] }}, {{ buildings[0][1] }}], 10);

        // Add map layer
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(mymap);

        // Add building markers
        {% for building in buildings %}
            L.marker([{{ building[0] }}, {{ building[1] }}])
                .bindPopup('building: {{ building[2] }} <br> protection score: {{ building[3] }}')
                .addTo(mymap);
        {% endfor %}
    </script>
</body>
</html>
