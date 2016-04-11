import digitalocean
manager = digitalocean.Manager(token="9cc0208709c43e877b89986a585df7eb2c4050fafc07469680812e3706608a40")
my_droplets = manager.get_all_droplets()
print my_droplets