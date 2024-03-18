# Format an output file for input into Pogo to make Genome Browser tracks
# Restructure the dataframe for input into Pogo
# Outputs are named first by TMT or TOM, their ID number, WTC11, then unfrac or 8frac

library(readr)
library(dplyr)
library(stringr)

##All AS192 Peptides
as192_peptide_summary_df <- read_csv("./data/as192_annotations_table_1.csv")

restructured_pogo_df <- as192_peptide_summary_df %>%
  mutate( #mutate just allows us to modify and add columns!
    Experiment = "AS192", #create column called "Experiment" that is filled with the experiment type
    PSMs = 1, #create column called "PSMs" and fill with 1
    Quant = 1 #create column called "Quant" and fill with 1
  ) %>%
  select(Experiment, Distinct_Peptide = Peptide, PSMs, Quant) #the dataframe we're creating will only have these columns

file_path <- "./results/Pogo_Peptides/as192_annotations.txt"
write.table(restructured_pogo_df, file = file_path, sep = "\t", quote = FALSE, row.names = FALSE)


##DDA Peptides
dda_peptides <- read_csv("./data/DDA_peptides.csv")

restructured_pogo_df <- dda_peptides %>%
  mutate( #mutate just allows us to modify and add columns!
    Experiment = "DDA", #create column called "Experiment" that is filled with the experiment type
    PSMs = 1, #create column called "PSMs" and fill with 1
    Quant = 1 #create column called "Quant" and fill with 1
  ) %>%
  select(Experiment, Distinct_Peptide = Peptides, PSMs, Quant) #the dataframe we're creating will only have these columns

file_path <- "./results/Pogo_Peptides/DDA_peptides.txt"
write.table(restructured_pogo_df, file = file_path, sep = "\t", quote = FALSE, row.names = FALSE)


##Tomahto Peptides
tomahto_peptides <- read_csv("./data/Tomahto_peptides.csv")

restructured_pogo_df <- tomahto_peptides %>%
  mutate( #mutate just allows us to modify and add columns!
    Experiment = "Tomahto", #create column called "Experiment" that is filled with the experiment type
    PSMs = 1, #create column called "PSMs" and fill with 1
    Quant = 1 #create column called "Quant" and fill with 1
  ) %>%
  select(Experiment, Distinct_Peptide = Peptides, PSMs, Quant) #the dataframe we're creating will only have these columns

file_path <- "./results/Pogo_Peptides/tomahto_peptides.txt"
write.table(restructured_pogo_df, file = file_path, sep = "\t", quote = FALSE, row.names = FALSE)
