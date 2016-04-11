import paramiko
import keyring
import sys
import os

# Connect via SSH
hostname = '10.211.55.33'
port = 22
username = 'root'
privatekey = '/Users/thebig/.ssh/id_rsa'

## Keyfile Expand
keyfile = os.path.expanduser(privatekey)
password = keyring.get_password('SSH', keyfile)
key = paramiko.RSAKey.from_private_key_file(keyfile, password=password)
## Keyfile Expand
client = paramiko.Transport((hostname, port))
#Connect via SSH
try:
    print "connecting..."
    pass
    client.connect(username=username, pkey=key)
    print "output", stdout.read()
except Exception, e:
    print 'Failed loading' % (privatekey, e)

# try:
#     client.connect(username=username, pkey=key, timeout=5)
#     print "output: ", stdout.read()
# except paramiko.SSHException, e:
#     print "Password is invalid:", e
# except paramiko.AuthenticationException:
#     print "Authentication failed for some reason"
# except socket.error, e:
#     print "Socket connection failed:", e



client.close()