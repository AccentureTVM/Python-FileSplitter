#!/usr/bin/python

import sys

def main(argv):
	inputfile = ''
	
	if len(sys.argv) != 3:
		print 'test.py <inputfile> <lines per file>'
		sys.exit(2)
	inputfile = argv[1]
	linesper = int(argv[2])
	linecount = 0
	filecount = 1
	
	output = inputfile.rsplit('.',1)
	extension = "." + output[1]
	output = output[0]
	
	fo = open(output + "_" + str(filecount) + extension, 'w+')
	fi = open(inputfile, 'r')
	for line in fi.readlines():
		if linecount == linesper:
			fo.close()
			filecount += 1
			s = output + "_" + str(filecount) + extension
			fo = open(s, 'w+')
			linecount = 0
		linecount += 1
		fo.write(line)
		

	
	fo.close()
	
if __name__ == "__main__":
   main(sys.argv)
