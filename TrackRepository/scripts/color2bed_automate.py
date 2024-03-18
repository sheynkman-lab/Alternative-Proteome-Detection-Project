import csv
import argparse

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Convert BED file to BED12 format and add RGB colors.')
    parser.add_argument('--bed_file_path', required=True, help='Path to the input BED file')
    parser.add_argument('--csv_file_path', required=True, help='Path to the CSV file with peptide sequences')
    parser.add_argument('--output_bed12_path', required=True, help='Path to the output BED12 file')
    parser.add_argument('--track_name', required=True, help='Track name for the BED12 file')
    args = parser.parse_args()

    # Define the RGB colors for major and minor isoforms
    major_color = "0,153,136"
    minor_color = "238,119,51"

    # Create a dictionary to store the isoform information from the CSV file
    isoform_dict = {}

    # Read the CSV file and populate the isoform dictionary
    with open(args.csv_file_path, 'r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            # Check if the 'Peptide' column is present
            if 'Peptide' not in row:
                raise ValueError("Column 'Peptide' not found in the CSV file.")

            isoform_dict[row['Peptide'].strip()] = row['is_major_gene_isoform']

    # Update the BED file and convert it to BED12 format
    with open(args.bed_file_path, 'r') as bed_file, open(args.output_bed12_path, 'w') as output_bed12_file:
        # Write the track line at the top of the file
        output_bed12_file.write(f"track name={args.track_name} itemRgb=On\n")

        for line in bed_file:
            # Split the BED line into columns
            columns = line.strip().split('\t')

            # Get the name (Peptide) from the BED file
            name = columns[3]

            # Check if the name exists in the isoform dictionary
            if name in isoform_dict:
                # Get the is_major_gene_isoform value
                is_major = isoform_dict[name]

                # Set the RGB color based on the isoform type
                rgb_color = major_color if is_major == "TRUE" else minor_color

                # Update the RGB color column in the BED line
                columns[8] = rgb_color

            # Convert the BED line to BED12 format
            bed12_columns = columns[:6] + [columns[6], columns[7], columns[8]] + columns[9:]

            # Write the updated BED12 line to the output file
            output_bed12_file.write('\t'.join(bed12_columns) + ',\n')

    print("RGB colors added, BED file converted to BED12 format, and track line added.")

if __name__ == "__main__":
    main()
