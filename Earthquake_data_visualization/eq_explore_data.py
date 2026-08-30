from pathlib import Path
import json
import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path('eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Creating map
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title="Global Earthquake", color=mags, color_continuous_scale='Viridis',
                     labels={'color': 'Magnitude'}, projection='natural earth'
                    )
fig.show()