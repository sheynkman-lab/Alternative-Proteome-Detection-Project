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
Raw sequencing data files can be found in the National Institutes of Health (NIH) National Library of Medicine’s Sequence Read Archive with the project accession number [PRJNA1090880](https://www.ncbi.nlm.nih.gov/sra/SRX24041640[accn]) <br />

## Mass Spectrometry Data Analysis

Mass spectrometry raw files, Proteome Discoverer PSM result files, and Tomahto result files have been deposited to the ProteomeXchange Consortium via the [PRIDE archive](https://www.ebi.ac.uk/pride/archive) using accessions PXD050904 and PXD050909. Data will become available upon publication of the manuscript in JASMS. <br />

Analysis of the mass spectrometry data was conducted using custom R scripts. Associated scripts and supporting files can be found in [`/MassSpectrometryAnalysis`](https://github.com/sheynkman-lab/Alternative-Proteome-Detection-Project/tree/93ee40266c1a9dc28cb5e744c9609c4c66c8e4ce/MassSpectrometryAnalysis). 

## Statistical Software
The R script used to create area-proportional Venn diagrams comparing the DDA and Tomahto results can be found in [`/scripts/DDA_vs_Tomahto.Rmd`](https://github.com/sheynkman-lab/Alternative-Proteome-Detection-Project/blob/main/scripts/DDA_vs_Tomahto.Rmd).

## Peptide-to-protein isoform genome browser track
The BED files used to create the [UCSC Genome Browser track](https://www.genome.ucsc.edu/s/emilyfwatts/Alternative%2DProteome%2DDetection) that accompanies this manuscript can be found in [`/TrackRepository`](https://github.com/sheynkman-lab/Alternative-Proteome-Detection-Project/tree/main/TrackRepository). All scripts used to create these files using custom python scripts and [Pogo](https://www.sanger.ac.uk/tool/pogo/) can be found under [`/TrackRepository/scripts`](https://github.com/sheynkman-lab/Alternative-Proteome-Detection-Project/tree/main/TrackRepository/scripts).

