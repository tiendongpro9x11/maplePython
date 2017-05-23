import pexpect
MW = "/home/rues/maple2016/bin/maple -tu"
def maple(X):
	child = pexpect.spawn(MW)
	child.expect('#--')
	child.sendline(X)
	child.expect('#--')
	out = child.before
	out = out[out.find(';')+1:].strip()
	out = ''.join(out.split('\r\n'))
	return out