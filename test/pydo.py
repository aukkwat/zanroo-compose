from digitalocean import ClientV2
client = ClientV2(token='9cc0208709c43e877b89986a585df7eb2c4050fafc07469680812e3706608a40')

list = client.droplets.all()
print list['meta']['total']

print list['droplets'][3]['networks']['v4'][0]['ip_address']
print list['droplets'][3]['networks']['v4'][1]['ip_address']