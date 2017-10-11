import sys
from pwn import *

if len(sys.argv) < 2:
        log.failure("Usage: level1.py <bandit1 password>")
        sys.exit()

host = 'bandit.labs.overthewire.org'
username = 'bandit1'
password = sys.argv[1]

shell = ssh(host = host, user = username, password = password, port = 2220)
log.info("List dir: %s\n" % shell.ls(['-la']))
log.success("Password: %s" % shell.cat(['./-']))
shell.close()
