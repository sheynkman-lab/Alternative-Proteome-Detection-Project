cd /Users/emilywatts/Library/CloudStorage/OneDrive-UniversityofVirginia/Grad_student_projects/Jennifer_AltProtDet/Final_GenomeBrowserTrack
export PATH=$PATH:/Users/emilywatts

gtfToGenePred ./data/wtc11_with_cds.gtf ./results/wtc11_gtf2bed/wtc11.genepred
genePredtoBed ./results/wtc11_gtf2bed/wtc11.genepred ./results/wtc11_gtf2bed/wtc11.bed