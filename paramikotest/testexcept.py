try:
    print "connecting..."
    client.close()
    import oss
except NameError, fd:
    print str(fd)
except ImportError, df:
    print str(df)
    raise
finally:
    print "Final"

# Command to Action
# stdin, stdout, stderr = ssh.exec_command(cmd)