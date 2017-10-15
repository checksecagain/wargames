import sys
from pwn import *

def level0_to_level1(shell):
	log.info("List dir: %s\n" % shell.ls(['-la']))
	log.success("Flag: %s" % shell.cat(['readme']))

def level1_to_level2(shell):
	log.info("List dir: %s\n" % shell.ls(['-la']))
	log.success("Flag: %s" % shell.cat(['./-']))

def level2_to_level3(shell):
	log.info("List dir: %s\n" % shell.ls(['-la']))
	log.success("Flag: %s" % shell.cat(['spaces in this filename']))

def level3_to_level4(shell):
	log.info('inhere directory listing: %s\n' % shell.ls(['inhere', '-la']))
	log.success('Flag: %s' % shell.cat(['inhere/.hidden']))

def level4_to_level5(shell):
	log.info(shell.ls(['inhere', '-la']))
	log.info(shell.find(['./inhere', '-type', 'f', '-exec', 'file', '{}', '+']))
	log.success('Flag: %s' % shell.cat(['./inhere/-file07']))

def level5_to_level6(shell):
	log.success('Flag: %s' % shell.find('inhere/ -type f -size 1033c -exec cat {} +'))

def level6_to_level7(shell):
	log.success('Flag: %s' % shell.find('/ -type f -group bandit6 -user bandit7 -size 33c -exec cat {} + 2> /dev/null'))

def level7_to_level8(shell):
	log.success('Flag: %s' % shell.cat('data.txt | grep millionth'))

def level8_to_level9(shell):
	shell.interactive()

def main():
	if len(sys.argv) != 3:
       		log.failure("Usage: %s <user> <password>" % (__file__))
        	sys.exit(1)

	host = 'bandit.labs.overthewire.org'
	username = sys.argv[1]
	password = sys.argv[2]
	port = 2220

	shell = ssh(host = host, user = username, password = password, port = port)
	log.success("Logged in as %s" % shell.whoami())

	if username == 'bandit0':
		level0_to_level1(shell)
	elif username == 'bandit1':
		level1_to_level2(shell)
	elif username == 'bandit2':
		level2_to_level3(shell)
	elif username == 'bandit3':
		level3_to_level4(shell)
	elif username == 'bandit4':
		level4_to_level5(shell)
	elif username == 'bandit5':
		level5_to_level6(shell)
	elif username == 'bandit6':
		level6_to_level7(shell)
	elif username == 'bandit7':
		level7_to_level8(shell)
	elif username == 'bandit8':
		level8_to_level9(shell)

	shell.close()

if __name__ == '__main__':
	main()

