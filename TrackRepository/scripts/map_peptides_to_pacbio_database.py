# script to convert pacbio database files (fasta, gtf) to one compatible for pogo peptide mapping


#%%

from Bio import SeqIO
import pandas as pd
import os


# Note - the data directory should contain five input files below
# Directory `data` is in ignored in git, so you will need to create it and put the files there

### input files
pacbio_fasta_file = "./data/wtc11_orf_refined.fasta"

pacbio_gtf_file = "./data/wtc11_with_cds.gtf"


### input file - extract ensg to gene map
# 62700 ensgs in the comprehensive gencode v44 gtf found
ensg_to_gene_file = "./data/ensg_to_gene_name_map.txt"
gene_to_ensg = dict()
for line in open(ensg_to_gene_file):
    ensg = line.split('\t')[0].split('.')[0]
    gene = line.split('\t')[1].strip()
    gene_to_ensg[gene] = ensg 


### Output Files
### Results are output into a directory called `results` in the current working directory

# Define the directory paths
output_directory = "./results/"
pacbio_fasta_prefix = output_directory + "wtc11_orf_refined"
pacbio_gtf_prefix = output_directory + "wtc11_with_cds"

# Check if the output directory exists and create it if it doesn't
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

### ensure that all pb accessions in the gtf are found in the fasta file and vice versa

# read in pacbio accession mapping info in the fasta file 
sequences = SeqIO.parse(pacbio_fasta_file, "fasta")
pb_and_gene_from_fasta = dict()
for seq in sequences:
    pb_acc = seq.description.split('|')[1]
    gene = seq.description.split('GN=')[1].strip()
    pb_and_gene_from_fasta[pb_acc] = gene

# note for jennifer's smc fasta - 96076 unique pb accessions


### read in pacbio accession mapping info from the gtf file

pb_info_from_gtf = dict()
for line in open(pacbio_gtf_file):
    genename_from_gtf = line.split('gene_id "')[1].split('"')[0]
    pb_accession_from_gtf = line.split('transcript_id "')[1].split('|')[1]
    pb_descriptor_from_gtf = line.split('transcript_id "')[1].split('"')[0]
    pb_info_from_gtf[pb_accession_from_gtf] = (genename_from_gtf, pb_descriptor_from_gtf)

# note for jennifer's smc gtf - 87729 unique pb accessions


# create a set of all pacbio accessions from both the fasta and gtf files
all_pb_accessions = set(pb_and_gene_from_fasta.keys()) | set(pb_info_from_gtf.keys())

# assign unique ENSTs to each pb accession
pb_to_enst = dict()
for index, pacbio_accession in enumerate(list(sorted(all_pb_accessions))):
    # assigning a unique ENST that is assumed to not exist in GENCODE, because starts with 9
    enst = 'ENST' + str(90000000000 + index)
    pb_to_enst[pacbio_accession] = enst


# next, before writing out all the files, retreive the ensg for each genename and ensure each pb accession has a genename
# in cases where pb accession genename is not found in the gencode-file-based ensg-to-genename map, assign a ensg based on the pb gene index
# in cases where pb accession genename is "nan" (because is a novel gene?), assign a ensg based on the pb gene index
# TODO



# for each pb accession, get the genename from the pacbio gtf or fasta file, or assign a temporary ensg 
pb_to_ensg = dict()
for pb_accession in all_pb_accessions:
    # first try to retrieve genename from gtf, then fasta
    if pb_accession in pb_info_from_gtf:
        genename_retrieved = pb_info_from_gtf[pb_accession][0]
    elif pb_accession in pb_and_gene_from_fasta:
        genename_retrieved = pb_and_gene_from_fasta[pb_accession]
    else:
        raise Exception(f'pb accession {pb_accession} not found in either gtf or fasta file')

    # next, retrieve or assign new ensg
    if genename_retrieved in gene_to_ensg:
        ensg = gene_to_ensg[genename_retrieved]
    else:
        # when assigning a new ensg, start with 90000000000 plus the index of the pb gene
        pb_accession_gene_index = int(pb_accession.split('.')[1])
        ensg = 'ENSG' + str(90000000000 + pb_accession_gene_index)
    
    pb_to_ensg[pb_accession] = ensg
    

# write out tll information from gtf, fasta, and the newly assigned enst to pacbio mapping
with open(output_directory + 'PacBio_Database_to_PoGo_Compatible_Output_Info_Table.tsv', 'w') as ofile:
    column_names = ['PacBio_Accession', 'Genename_from_GTF', 'Genename_from_FASTA', f'ENSG_from_GC', 'PacBio_Descr_from_GTF', 'In_GTF', 'In_FASTA']
    ofile.write('\t'.join(column_names) + '\n')

    for pb_accession in all_pb_accessions:
        genename_from_gtf = pb_info_from_gtf.get(pb_accession, ('', ''))[0]
        genename_from_fasta = pb_and_gene_from_fasta.get(pb_accession, '')
        ensg_from_gencode = gene_to_ensg.get(genename_from_gtf, '')
        pb_descr_from_gtf = pb_info_from_gtf.get(pb_accession, ('', ''))[1]
        in_gtf = 'yes' if pb_accession in pb_info_from_gtf else 'no'
        in_fasta = 'yes' if pb_accession in pb_and_gene_from_fasta else 'no'
        ofile.write('\t'.join([pb_accession, genename_from_gtf, genename_from_fasta, ensg_from_gencode, pb_descr_from_gtf, in_gtf, in_fasta]) + '\n')



# write out PoGo-compatible FASTA file
with open(pacbio_fasta_prefix + '_PoGo_compatible.fasta', 'w') as ofile:
    for seq in SeqIO.parse(pacbio_fasta_file, 'fasta'):
        pb_accession = seq.description.split('|')[1]
        genename = seq.description.split('GN=')[1].strip()
        enst = pb_to_enst[pb_accession]
        ensg = pb_to_ensg[pb_accession]
        ofile.write(f'>ENSP|{enst}|{ensg}|{seq.description}\n{seq.seq}\n')

# write out PoGo-compatible GTF file
tmp_gtf_file = pacbio_gtf_prefix + '_PoGo_compatible_tmp.gtf'
with open(tmp_gtf_file, 'w') as ofile:
    for line in open(pacbio_gtf_file):
        pb_accession = line.split('transcript_id "')[1].split('|')[1]
        enst = pb_to_enst[pb_accession]
        ensg = pb_to_ensg[pb_accession].split('.')[0]
        fields = line.split('\t')
        ofile.write('\t'.join(fields[:8]) + '\t' + f'gene_id "{ensg}"; transcript_id "{enst}";\n')

# Note that the GTF file needs to be properly formatted and sorted
# #1 - gene lines need to be added
# #2 - exon/cds coordinates need to be sorted in ascending order

# read in tmp gtf again to do the sorting and final write out
columns = ["seqname", "source", "feature", "start", "end", "score", "strand", "frame", "attribute"]
df = pd.read_csv(tmp_gtf_file, sep="\t", comment="#", header=None, names=columns)
df['ensg'] = df['attribute'].apply(lambda x: x.split('gene_id "')[1].split('"')[0]) 
df['enst'] = df['attribute'].apply(lambda x: x.split('transcript_id "')[1].split('"')[0])

# Define the function to insert a new gene feature row before the start of the gene block
def insert_gene_row(group):
    start = group['start'].min()
    end = group['end'].max()
    strand = group['strand'].unique()[0]
    seqname = group['seqname'].unique()[0]
    source = group['source'].unique()[0]
    feature = 'gene'
    attr = 'gene_id "' + group['ensg'].unique()[0] + '";'

    # Create the gene row
    gene_row = pd.DataFrame([[seqname, source, feature, start, end, '.', strand, '.', attr]], columns=columns)  

    # Concatenate the gene row with the original group
    return pd.concat([gene_row, group], sort=False, ignore_index=True)


df.groupby(['enst', 'feature'], sort=False).apply(lambda x: x.sort_values('start', inplace=True)).reset_index(drop=True)

df_with_gene_rows = df.groupby('ensg').apply(insert_gene_row).reset_index(drop=True)
df_out = df_with_gene_rows.drop(columns=['ensg', 'enst'])

final_gtf_file = tmp_gtf_file.replace('_PoGo_compatible_tmp.gtf', '_PoGo_compatible.gtf')
df_out.to_csv(final_gtf_file, sep='\t', index=False, quoting=3, header=False)


# remove the tmp file
if os.path.exists(tmp_gtf_file):
   os.remove(tmp_gtf_file)