import dosa
import json

API_KEY = '9cc0208709c43e877b89986a585df7eb2c4050fafc07469680812e3706608a40'
# dosa.set_debug()  # enables debug logs

client = dosa.Client(api_key=API_KEY)

# Droplets
client.droplets.list()
# status, result = client.droplets.create(name='terminator', region='nyc2',\
#     size='512mb', image='ubuntu-14-04-x32', ssh_keys=[12345])
# new_droplet_id = result['id']

# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(client.images.list())
# parsed = json.loads(client.droplets.list())
# print parsed
print client.droplets.list()
# print json.dumps(parsed, indent=4, sort_keys=True)

# status, result = client.droplets.create(name='terminator', region='nyc2',\
#     size='512mb', image='ubuntu-14-04-x32', ssh_keys=[12345])
# new_droplet_id = result['id']