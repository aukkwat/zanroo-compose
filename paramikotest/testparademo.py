import paramiko

client = paramiko.SSHClient
client.connect(hostname='zanroo',username='root',password='bigmaster')
client.load_system_host_keys()
stdin, stdout, stderr = client.exec_command('ls -l')