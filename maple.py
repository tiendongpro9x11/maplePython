import pexpect
import os

def maple(X):
	with open(os.getcwd()+"/linkmaple.txt") as F:
		MAPLEDIR = F.readline()
	MW = MAPLEDIR + " -tu"
	child = pexpect.spawn(MW)
	child.expect('#--')
	child.sendline(X)
	child.expect('#--')
	out = child.before
	out = out[out.find(';')+1:].strip()
	out = ''.join(out.split('\r\n'))
	return out