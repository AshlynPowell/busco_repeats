# Insect Genome Repetitive Elements

`condense_buscos.py` compiles BUSCO sequences from a given assembly into a single file. The script takes in an accession number, opens each sequence file in the associated BUSCO results, and writes each sequence to an outfile formatted for BLAST (if a multi-copy BUSCO, only the first sequence is written to the file).

`busco_blast_bokeh.sh` and `protein_blast.sh` are scripts that run their respective blast calls and bokeh visualization scripts. Comments in the scripts describe command line arguements that should be passed in to each script.

`visualize_busco_blast.sh` and `visualize_protein_blast.sh` are scripts that each use bokeh to visualize data in multiple ways (histogram, lineplot, table). `visualize_protein_blast.sh` outputs a summary of hits to `TE_regulation_genes.csv`

`genomes.txt` contains a list of all 441 insect genome assemblies used in this study. You can run the other scripts over this list, e.g. for i in `cat genomes.txt; do python visualize_busco_blast.py $i; done`
