from pwn import *

shell = ssh(host='bandit.labs.overthewire.org', user='bandit0', password='bandit0', port=2220)

log.info("username: %s" % shell.whoami())
log.info("pwd: %s" % shell.pwd())

print shell['cat readme']
