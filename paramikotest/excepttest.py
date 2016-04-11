import paramiko
import logging
logging.basicConfig()

host = '10.211.55.33'
username = 'root'
password = 'bigmaster'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect(host, username=username, password=password)
except paramiko.SSHException:
    print "Connection Error"

ssh.close()