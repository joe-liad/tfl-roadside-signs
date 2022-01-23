import pandas as pd
df = pd.read_xml('./signs.xml', xpath=".//doc:Sign", namespaces= {'doc':"http://www.tfl.gov.uk/vms/1.0"})
js = df.to_json('./signs.json', orient='records', indent=4)