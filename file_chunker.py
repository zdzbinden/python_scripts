#!/usr/bin/env python3.6
import sys

def file_chunker(infile, chunks):

# read file from command line
	with open(infile) as file_object:	

#count number of loci	
		loci_count = 1
		chunks = int(sys.argv[2])
		
		for line in file_object:
			if line[0] == ">":
				pass	
			else:
				loci_count = loci_count+1

		chunk_size = loci_count // chunks

#write .loci file into chunk files 
	with open(infile) as file_object:
		max_chunks = int(sys.argv[2])
		chunks = 1
		loci_number = 1
		
		for line in file_object:
			
			if chunks < max_chunks:
				
				if loci_number <= chunk_size:
					if line[0] == ">":
						print(line.strip(), file=open(str(chunks) + ".chunk", "a"))
			
					else:
						loci_number = loci_number + 1
						print("", file=open(str(chunks) + ".chunk", "a"))
				else:	
					loci_number = 1
					chunks = chunks + 1 
					print(line.strip(), file=open(str(chunks) + ".chunk", "a"))
			
			else:
				chunks = max_chunks
				print(line.strip(), file=open(str(chunks) + ".chunk", "a"))

file_chunker(sys.argv[1], sys.argv[2])
