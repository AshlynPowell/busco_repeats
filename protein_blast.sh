#!/bin/bash

#SBATCH --time=72:00:00   # walltime
#SBATCH --ntasks=1   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=4096M   # memory per CPU core
#SBATCH -J "busco_data.job"   # job name
#SBATCH --mail-user=ashlynpowell913@gmail.com   # email address
#SBATCH --mail-type=FAIL


# Set the max number of threads to use for programs using OpenMP. Should be <= ppn. Does nothing if the program doesn't use OpenMP.
export OMP_NUM_THREADS=$SLURM_CPUS_ON_NODE

# LOAD MODULES, INSERT CODE, AND RUN YOUR PROGRAMS HERE

source ~/.bashrc
conda activate blast

#	If files are in different directories add full path to each
#	Script takes in genome name, then Piwi and Ago1 protein sequences from command line
#	Output file is named using genome and protein + .blast.out

#	Make blast database if needed with the following command:
#		makeblastdb -dbtype nucl -in $1
tblastn -db $1 -query $2 -out /fslhome/anp37/compute/results/$1.$2.blast.out -outfmt 7
tblastn -db $1 -query $3 -out /fslhome/anp37/compute/results/$1.$3.blast.out -outfmt 7

#	Visualize blast results with bokeh script
conda activate bokeh
python visualize_protein_blast.py $1.Piwi_protein.txt.blast.out $1.Ago1_protein.txt.blast.out