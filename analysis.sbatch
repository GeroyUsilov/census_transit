#!/bin/bash
#SBATCH --job-name=analysis
#SBATCH --output=analysis.out
#SBATCH --error=analysis.err
#SBATCH --account=pi-amurugan
#SBATCH --time=00:1:30
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=1000

module load python
python station_script.py $1