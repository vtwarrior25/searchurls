import json
import pprint

filename="urls.json"
browsercmd="firefox"

with open(filename) as json_data:
  data=json.loads(json_data)
  json_data.close
  pprint(data)  


