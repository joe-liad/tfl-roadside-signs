import pandas as pd
from pyproj import Proj, transform

# Longitude,Latitude = transform(Proj(init='epsg:28800'), Proj(init='epsg:4326'), Northing, Easting)

# extract the signs array only (not the feed metadata) from the xml file
df = pd.read_xml('./signs.xml', xpath=".//doc:Sign", namespaces= {'doc':"http://www.tfl.gov.uk/vms/1.0"})

# convert location coordiantes from BNG to WGS84 for easier web mapping
df['easting'], df['northing'] = transform(Proj(init='epsg:27700'), Proj(init='epsg:4326'), df['easting'], df['northing'])
df.rename(columns = {'easting':'longitude', 'northing':'latitude'}, inplace = True)

# write the array to pretty printed json (easier to diff than csv rows)
js = df.to_json('./signs.json', orient='records', indent=4)