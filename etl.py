import pandas as pd
# extract the signs array only (not the feed metadata) from the xml file
df = pd.read_xml('./signs.xml', xpath=".//doc:Sign", namespaces= {'doc':"http://www.tfl.gov.uk/vms/1.0"})
# write the array to pretty printed json (easier to diff than csv rows)
js = df.to_json('./signs.json', orient='records', indent=4)