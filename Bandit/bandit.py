import sys
from pwn import *

def level0_to_level1(shell):
	log.info("List dir: %s\n" % shell.ls(['-la']))
	flag = shell.cat(['readme'])
	log.success("Flag: %s" % flag)

def level1_to_level2(shell):
	log.info("List dir: %s\n" % shell.ls(['-la']))
	flag = shell.cat(['./-'])
	log.success("Flag: %s" % flag)

def level2_to_level3(shell):
	log.info("List dir: %s\n" % shell.ls(['-la']))
	flag = shell.cat(['spaces in this filename'])
	log.success("Flag: %s" % flag)

def level3_to_level4(shell):
	log.info('inhere directory listing: %s\n' % shell.ls(['inhere', '-la']))
	flag = shell.cat(['inhere/.hidden'])
	log.success('Flag: %s' % flag)

def level4_to_level5(shell):
	log.info(shell.ls(['inhere', '-la']))
	log.info(shell.find(['./inhere', '-type', 'f', '-exec', 'file', '{}', '+']))
	flag = shell.cat(['./inhere/-file07'])
	log.success('Flag: %s' % flag)

def level5_to_level6(shell):
	flag = shell.find('inhere/ -type f -size 1033c -exec cat {} +')
	log.success('Flag: %s' % flag)

def level6_to_level7(shell):
	flag = shell.find('/ -type f -group bandit6 -user bandit7 -size 33c -exec cat {} + 2> /dev/null')
	log.success('Flag: %s' % flag)

def level7_to_level8(shell):
	flag = shell.cat('data.txt | grep millionth')
	log.success('Flag: %s' % flag)

def level8_to_level9(shell):
	flag = shell.cat('data.txt | sort | uniq -u')
	log.success('Flag: %s' % flag)
	
def level9_to_level10(shell):
	flag = shell['strings data.txt | grep ==']
	log.success('Flag:\n %s' % flag)

def level10_to_level11(shell):	
	flag = shell['base64 -d data.txt']
	log.success('Flag: %s' % flag)

def level11_to_level12(shell):
	flag = shell["cat data.txt | tr 'a-mn-zA-MN-Z' 'n-za-mN-ZA-M'"]
	log.success('Flag: %s' % flag)
	#shell.interactive()

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
	elif username == 'bandit9':
		level9_to_level10(shell)
	elif username == 'bandit10':
		level10_to_level11(shell)
	elif username == 'bandit11':
		level11_to_level12(shell)

	shell.close()

def god_mode(shell, host, username, password, port):
	flag = level0_to_level1(shell)
	shell = ssh(host = host, user = username, password = password, port = port)


if __name__ == '__main__':
	main()

