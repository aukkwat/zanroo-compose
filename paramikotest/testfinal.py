import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='zanroo', username='root', password='bigmaster')
stdin, stdout, stderr = ssh.exec_command('ls')
print 'This is output =',stdout.readlines()
print 'This is error =',stderr.readlines()
ssh.close()