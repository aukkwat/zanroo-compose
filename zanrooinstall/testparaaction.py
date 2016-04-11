import zrconnect
import sys

# Access variables.
hostname = 'zanroo'
port = 22
username = 'root'
password = 'bigmaster'
sudo_password = password  # assume that it is the same password

# Create the SSH connection
ssh = zrconnect.MySSH()
ssh.set_verbosity(False)
ssh.connect(hostname=hostname,
            username=username,
            password=password,
            port=port)
if ssh.connected() is False:
    print 'ERROR: connection failed.'
    sys.exit(1)


def run_cmd(cmd, indata=None):
    '''
    Run a command with optional input.

    @param cmd    The command to execute.
    @param indata The input data.
    @returns The command exit status and output.
             Stdout and stderr are combined.
    '''
    print
    print '-' * 128
    print 'command: %s' % (cmd)
    status, output = ssh.run(cmd, indata)
    print 'status : %d' % (status)
    print 'output : %d bytes' % (len(output))
    print '-' * 128
    print '%s' % (output)


run_cmd('ls /')