cd /Users/emilywatts/Library/CloudStorage/OneDrive-UniversityofVirginia/Grad_student_projects/Jennifer_AltProtDet/Final_GenomeBrowserTrack
export PATH=$PATH:/Users/emilywatts

#AS192
PoGo -fasta ./results/wtc11_orf_refined_PoGo_compatible.fasta -gtf ./results/wtc11_with_cds_PoGo_compatible.gtf -in ./results/PoGo_Peptides/as192_annotations.txt -format BED

#DDA
PoGo -fasta ./results/wtc11_orf_refined_PoGo_compatible.fasta -gtf ./results/wtc11_with_cds_PoGo_compatible.gtf -in ./results/PoGo_Peptides/DDA_peptides.txt -format BED

#TOMAHTO
PoGo -fasta ./results/wtc11_orf_refined_PoGo_compatible.fasta -gtf ./results/wtc11_with_cds_PoGo_compatible.gtf -in ./results/PoGo_Peptides/tomahto_peptides.txt -format BED

