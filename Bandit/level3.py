import sys
from pwn import *

user = 'bandit3'
host = 'bandit.labs.overthewire.org'

if len(sys.argv) != 2:
        log.failure("Usage: %s <%s password>" % (__file__, user))
        sys.exit()

#password = sys.argv[1]
password = 'UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK'
port = 2220

shell = ssh(host = host, user = user, password = password, port = port)
log.info('inhere directory listing: %s\n' % shell.ls(['inhere', '-la']))
log.success('Password: %s' % shell.cat(['inhere/.hidden']))
shell.close()

