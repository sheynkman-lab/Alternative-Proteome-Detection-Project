# Alternative Proteome Detection Analysis 
This repository contains scripts and files accompanying the manuscript [IS-PRM-based peptide targeting informed by long-read sequencing for alternative proteome detection](https://doi.org/10.1101/2024.04.01.587549).

## Long-read Proteogenomic (LRP) analysis
The [LRP pipeline](https://github.com/sheynkman-lab/Long-Read-Proteogenomics) [previously described by our group](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-022-02624-y) was run on this dataset using the Nextflow workflow.
```
git clone https://
.com/sheynkman-lab/Long-Read-Proteogenomics
cd Long-Read-Proteogenomics
nextflow run main.nf --config conf/test_with_sqanti.config
```

## DDA data analysis
*need to ask Jennifer about this -EFW*

## Tomahto data analysis
*need to ask Jennifer about this -EFW*

## Peptide-to-protein isoform genome browser track
The BED files used to create the [UCSC Genome Browser track](https://www.genome.ucsc.edu/s/emilyfwatts/Alternative%2DProteome%2DDetection) that accompanies this manuscript can be found in [`/TrackRepository`](https://github.com/sheynkman-lab/Alternative-Proteome-Detection-Project/tree/main/TrackRepository). All scripts used to create these files using custom python scripts and Pogo can be found under [`/TrackRepository/scripts`](https://github.com/sheynkman-lab/Alternative-Proteome-Detection-Project/tree/main/TrackRepository/scripts).

## Statistical Software
The R script used to create area-proportional Venn diagrams comparing the DDA and Tomahto results can be found in [`/scripts/DDA_vs_Tomahto.Rmd`](https://github.com/sheynkman-lab/Alternative-Proteome-Detection-Project/blob/main/scripts/DDA_vs_Tomahto.Rmd).

