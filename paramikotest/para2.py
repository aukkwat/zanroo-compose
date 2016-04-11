import os
import paramiko
import getpass

user = os.getlogin()
print "Connecting via %s: what is your password?" % user
pw = getpass.getpass()
ssh = paramiko.SSHClient()
#ssh.load_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('centos64-1', username=user, password=pw)
stdin, stdout, stderr = ssh.exec_command('uname -a')
print "output", stdout.read()
ssh.close()
