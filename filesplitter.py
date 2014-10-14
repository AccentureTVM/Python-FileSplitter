#!/usr/bin/python

import sys
import argparse
import mmap

def main(argv):
	parser = argparse.ArgumentParser(description="Split files with equal number of lines")
	parser.add_argument('inputfile', help='the file to split')
	parser.add_argument('outputfile', nargs="?", help='The name of the split files. Default will be the same as the input file. Split files will have _# appended to file name')
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('-l', '--lines', type=int, help='number of lines per file')
	group.add_argument('-f', '--files', type=int, help='number of files to make')
	args = parser.parse_args()
	inputfile = args.inputfile
	
	linesper = args.lines
	filenum = args.files
	
	linecount = 0
	filecount = 1
	
	output = inputfile.rsplit('.',1)
	extension = "." + output[1]
	output = output[0]
	
	try:
		fo = open(output + "_" + str(filecount) + extension, 'w+')
		fi = open(inputfile, 'r+')
		if(filenum!= None):
			buf = mmap.mmap(fi.fileno(), 0)
			lines = 0
			readline = buf.readline
			while readline():
				lines += 1
			linesper = lines/filenum + 1
	except IOError as e:
    		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		sys.exit(1)
		
	for line in fi.readlines():
		if linecount == linesper:
			fo.close()
			filecount += 1
			s = output + "_" + str(filecount) + extension
			try:
				fo = open(s, 'w+')
			except IOError as e:
		    		print "I/O error({0}): {1}".format(e.errno, e.strerror)
				sys.exit(1)
			linecount = 0
		linecount += 1
		fo.write(line)
		
	fo.close()

	print("Split completed successfully\n{} files created.".format(filecount) )
	
if __name__ == "__main__":
   main(sys.argv)
