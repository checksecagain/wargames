import sys
from pwn import *

user = 'bandit2'
host = 'bandit.labs.overthewire.org'

if len(sys.argv) != 2:
	log.failure("Usage: %s <%s password>" % (__file__, user))
	sys.exit()

password = sys.argv[1]
port = 2220

shell = ssh(host = host, user = user, password = password, port = port)
log.info("List dir: %s\n" % shell.ls(['-la']))
log.success("Password: %s" % shell.cat(['spaces in this filename']))
shell.close()
