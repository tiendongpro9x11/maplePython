import os
import platform

def maple(X):
	
	with open(os.getcwd()+"/createMaple.mpl","w") as F:
		F.write(X)
	if platform.system() == "Windows":
		MAPLEDIR = "cmaple"
	elif platform.system() == "Linux":
		with open(os.getcwd()+"/linkmaple.txt") as F:
			MAPLEDIR = F.readline()
	MW = MAPLEDIR + " -tu createMaple.mpl > getMaple.txt"
	os.system(MW)
	with open(os.getcwd()+"/getMaple.txt") as F:
		out = F.readlines()
	out = [x.strip() for x in out]

	return out[1]