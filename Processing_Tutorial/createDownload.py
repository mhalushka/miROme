#!/usr/bin/python
import sys
# This python script will create shell script to queue downloads sequentially 
# The commands to download the runs are listed in the following file, user may change this name according to the needs or use sys.argv arguments to call it from the command line.
out = open("download_runs.sh", "w+")
out.write("#!/bin/bash\n") # Indicating that we are calling shell script.
out.write("\n")
userinfile = sys.argv[1]
# read each accession and write the command to download these accessions from NCBI
with open(userinfile, "r") as inf: 
	infile = inf.readlines()
	for i in infile:
		x = i.strip()
		#out.write("/gpfs/fs1/sfw2/sratoolkit/2.9.2/bin/fasterq-dump -e 40 -t temp " + str(x) + "\n") # This will specify the path to fasterq-dump, if you have path set globally, you could skip the absolute path and retain only fasterq-dump onwards 
		out.write("fasterq-dump -e 10 -t temp " + str(x) + "\n") # specify absolute path to fasterq-dump bin if required/command not found 
		out.write("gzip "+str(x)+".fastq\n") # This will zip the files to save storage space, if you have enough room in the server/workstation, you may skip this as well by commenting it out. 
		#print("rm -rf /home/apatil8/ncbi/public/sra/*") # optional if the user wants to clear the temporary space manually then they can uncomment this line.
