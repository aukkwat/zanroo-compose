import yaml


stram = open("zanroo.yaml", "r")
test = yaml.load(stram)['zanroo']
print test