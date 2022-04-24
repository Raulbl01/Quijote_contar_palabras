import random
import sys
import re
def main(infilename, outfilename):
	with open(infilename) as infile:
		count = 0
		for line in infile:
			count = count + len(re.findall(r'\w+',line))
		with open(outfilename, 'w') as outfile:
			outfile.write("El numero de palabras para el fichero {} es: {}".format(infilename,count))


if __name__=="__main__":
    if len(sys.argv)<3:
        print(f"Usage: {sys.arv[0]} <infilename> <outfilename> ")
        exit(1)
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
    main(infilename, outfilename)
