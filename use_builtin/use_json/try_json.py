import json

import pprint

z2_dict = {'+++': 123, '---': 312, '--=': {1, 2, 3}}
print(json.dumps(z2_dict, indent=4))
print(z2_dict)
pprint.pprint(z2_dict)
