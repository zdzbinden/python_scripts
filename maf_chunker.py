#!/usr/bin/env python3.6

# maf_chunker creates specified number of files containing equal numbers 
# of loci (unless there are remainder loci, which append to the last 
# chunk.
# 1 to n '.maf_chunk' files will be created

import sys
import os

def maf_chunker(infile, chunks):
# read file from command line
	with open(infile) as file_object:	

#count number of loci, loci_count = -1 so that header is not counted
		loci_count = -1
		chunks = int(sys.argv[2])
		
		for line in file_object:
			line = line.strip()
			
			if len(line) > 0:
				pass	
			else:
				loci_count = loci_count+1

		chunk_size = loci_count // chunks
		
#write .maf file into chunk files, with each chunk beginning with header	
#first read header

	with open(infile) as file_object:
		max_chunks = int(sys.argv[2])
		chunks = 0
		loci_number = 0
		individual = 1
		
		for line in file_object:
			line = line.strip()

#isolate header chunk	
			if loci_number == 0:
				if len(line) > 0:
					print(line.strip(), file=open(str(chunks) + ".maf_chunk", "a"))
				else:
					loci_number = loci_number + 1 
					chunks = chunks + 1 

#move to loci chunks
			else:
				
				if chunks < max_chunks:
				
					if loci_number <= chunk_size:
						
#print contents of header before printing loci of individual 1			
						if individual == 1 and chunks == 1:
							with open('0.maf_chunk') as header:
								for var in header:
									print(var.strip(), file=open(str(chunks) + ".maf_chunk", "a"))
								
							print("", file=open(str(chunks) + ".maf_chunk", "a"))
							print(line.strip(), file=open(str(chunks) + ".maf_chunk", "a"))

							individual = individual + 1 
							
						else:
							
							if len(line) > 0:
								print(line.strip(), file=open(str(chunks) + ".maf_chunk", "a"))
								individaul = individual + 1 
								
							else:
								loci_number = loci_number + 1
								individual = 1
								print("", file=open(str(chunks) + ".maf_chunk", "a"))
					else:	
						loci_number = 1
						chunks = chunks + 1
						individual = 1 
						
						with open('0.maf_chunk') as header:
								for var in header:
									print(var.strip(), file=open(str(chunks) + ".maf_chunk", "a"))
						print("", file=open(str(chunks) + ".maf_chunk", "a"))
						
						print(line.strip(), file=open(str(chunks) + ".maf_chunk", "a"))
				
				else:
					chunks = max_chunks
					print(line.strip(), file=open(str(chunks) + ".maf_chunk", "a"))

	os.remove("0.maf_chunk")

maf_chunker(sys.argv[1], sys.argv[2])





