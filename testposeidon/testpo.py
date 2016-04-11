import poseidon
import sys
import time
client = poseidon.connect(api_key='9cc0208709c43e877b89986a585df7eb2c4050fafc07469680812e3706608a40')

def key():
    for i in client.keys.list():
        print i['name'], i['id']

def img():
    for i in client.images.list():
        print i['slug'], i['id']

def vm():
    try:
        for i in client.droplets.list():
            print i['name'], i['networks']['v4'][0]['ip_address'], i['id']
    except IndexError, err:
        print 'null'

def privatehost():
    for i in client.droplets.list():
        print i['networks']['v4'][0]['ip_address'], str("    "), i['name']

def writeprivate():
    with open('doprivateip', 'w') as ph:
        sys.stdout = ph
        privatehost()

def zanrookey():
    print client.keys.list()[0]['public_key']

def testconnect():
    ssh = droplet

# Create a droplet
image_id = 15943510  # replace with your own
key_id = 778082  # e.g., client.keys.list()[0]['id']
def createvm():
    droplet = client.droplets.create(name='test', region='sgp1', size='512mb', image=image_id, ssh_keys=[key_id], private_networking=True)

def removevm():
    droplet = client.droplets.delete(id=12573858)

# removevm()
# time.sleep(5)

# createvm()
removevm()
vm()

# import poseidon as P
# client = P.connect()
# ssh_key_id = client.keys.list()[0]['id']
# droplet = client.droplets.create('example.changshe.io', 'sfo1', '512mb',
#                               'ubuntu-14-04-x64', ssh_keys=[ssh_key_id])
# domain = client.domains.create('example.changshe.io', droplet.ip_address)
# records = client.domains.records(domain['name'])
# records.create('A', data=droplet.ip_address)
# ssh = droplet.connect()
# ssh.apt('git python-pip')
# ssh.git(username='changhiskhan', repo='hello_world')
# ssh.chdir('hello_world')
# ssh.pip_r('requirements.txt')
# ssh.nohup('python app.py') # DNS takes a while to propagate
# print ssh.ps()
