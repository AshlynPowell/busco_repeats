# Insect Genome Repetitive Elements

`genomes.txt` contains a list of all 441 insect genome assemblies used in this study. 

`condense_buscos.py` complies BUSCO sequences from a given assembly into a single file. The script takes in an accession number, opens each sequence file in the associated BUSCO results, and writes each sequence to an outfile for BLAST in the following format:
* < BUSCO name
* Associated BUSCO sequence (if a multi-copy sequence, only the first is written to the file)