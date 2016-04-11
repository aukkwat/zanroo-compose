import skiff
import pdb
# Token
thebigkey = skiff.rig("9cc0208709c43e877b89986a585df7eb2c4050fafc07469680812e3706608a40")
# Variable to Get List   # Pattern >>>  s.<resource>.all()
droplets = thebigkey.Droplet.all()
images = thebigkey.Image.all()
size = thebigkey.Size.all()
sshkey = thebigkey.Key.all()
Action = thebigkey.Action.all()
#Choose or Pointer
pdb.set_trace()
print droplets


# DropletName=
# Region=
# Size=
# Image=
#
# C1 = thebigkey.Droplet.create(name=DropletName, region=Region, size=Size, image=15943679)

#Show Droplets (DropletName,PublicIP,PrivateIP,Size,Zone)
# print Action
# print dropid


#Show Droplet List
# def listdroplet():
#     for getdrop in droplets:
#         print getdrop
#
# #Function Get Droplet ID
# def getdropletid():
#     print GETID


# #Show Action List
# for getaction in Action:
#     print getaction

# #Show Images
# for getimg in images:
#     print getimg

#Show SSH Keys

#Show

#Create Droplet

# my_droplet = thebigkey.Droplet.create(name='thebigtest', region='sgp1', size='512mb', image=15943679)
# >>> <hello.world (#2012974) nyc1 - Ubuntu 14.04 x64 - 512mb>
# wait until droplet is created
# my_droplet.wait_till_done()
# # refresh network information
# my_droplet = my_droplet.refresh()

# thebigkey.Droplet.create(name='thebigtest', region='sgp1', size='512mb', image=15943679)

# Destroy Droplet
# thebigkey.Droplet.destroy_droplet(12339420)
# wait_till_done(5)

# listdroplet()


# # Get by ID
# my_image_id = 3101580
# my_image = thebigkey.Image.get(my_image_id)
# # Or by slug
# ubuntu_slug = 'ubuntu1404'
# ubuntu_image = thebigkey.Image.get(ubuntu_slug)
# # Or by search (not very intelligent; useful for REPL use)
# ubuntu_image = thebigkey.Image.get('Ubuntu 13.10')