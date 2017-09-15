#!/usr/bin/env python3.6
import sys
import Bio.Align
from Bio import Seq

def read_loci(infile):

	# make emptyp dictionary
	loci = Bio.Align.MultipleSeqAlignment([])

	# read file from command line
	with open(infile) as file_object:	
		
		for line in file_object:
			
			if line[0] == ">":
				identifier = line.split()[0]
				sequence = line.split()[1]
				loci.add_sequence(identifier, sequence)

			else:
				yield(loci)
				loci = Bio.Align.MultipleSeqAlignment([])
				break

for x in read_loci(sys.argv[1]):
	print(x)
