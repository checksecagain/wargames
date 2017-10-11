from pwn import *

host = 'bandit.labs.overthewire.org'
username = 'bandit0'
password = 'bandit0'

shell = ssh(host = host, user = username, password = password, port = 2220)
log.info("List dir: %s\n" % shell.ls(['-la']))
log.success("Password: %s" % shell.cat(['readme']))
shell.close()
