import os

def maple(X):
	with open(os.getcwd()+"/linkmaple.txt") as F:
		MAPLEDIR = F.readline()
	with open(os.getcwd()+"/createMaple.mpl","w") as F:
		F.write(X)
	MW = MAPLEDIR + " -tu createMaple.mpl > getMaple.txt"
	os.system(MW)
	with open(os.getcwd()+"/getMaple.txt") as F:
		out = F.readlines()
	out = [x.strip() for x in out]

	return out[1]