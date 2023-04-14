import os
import json
import yaml

with open( os.path.join(os.getcwd(),'config_contexts', 'platform_ios.yml'),'r') as handler:
    y = yaml.safe_load(handler)

    print(json.dumps(y))