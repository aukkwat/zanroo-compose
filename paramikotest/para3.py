#!/usr/bin/python
import os
import paramiko
import getpass
import socket

def get_host():
    target_host = []
    input = raw_input("What is your target host? ")
    for item in input.split(","):
        target_host.append(item.strip())
    return target_host

def get_credential():
    pw = ""
    user=os.getlogin()
    print "Connecting via [%s]: what is your password?" % user
    while not pw:
        pw = getpass.getpass()
    return (user, pw)


def ssh_connect():
    target_host = get_host()
    (user, pw) = get_credential()

    ssh = paramiko.SSHClient()
    #ssh.load_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for h in target_host:
        try:
            print "Connecting to %s ..." % h
            ssh.connect(h, username=user, password=pw)
            stdin, stdout, stderr = ssh.exec_command('uname -a')
            print "%s>" % h,stdout.read()
        except paramiko.SSHException, e:
            print "Password is invalid:" , e
        except paramiko.AuthenticationException:
            print "Authentication failed for some reason"
        except socket.error, e:
            print "Socket connection failed on %s:" % h, e
    ssh.close()
def main():
    ssh_connect()

if __name__ == '__main__':
    main()