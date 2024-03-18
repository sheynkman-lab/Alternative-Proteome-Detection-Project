import argparse

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Convert BED file to BED12 format and add RGB colors based on abundance.')
    parser.add_argument('--bed_file_path', required=True, help='Path to the input BED file')
    parser.add_argument('--output_bed12_path', required=True, help='Path to the output BED12 file')
    parser.add_argument('--track_name', required=True, help='Track name for the BED12 file')
    args = parser.parse_args()

    # Define the RGB colors for major and minor isoforms
    major_color = "0,153,136"
    minor_color = "238,119,51"

    # Create a dictionary to store the maximum abundance for each peptide
    max_abundance_dict = {}

    # Update the BED file and convert it to BED12 format
    with open(args.bed_file_path, 'r') as bed_file, open(args.output_bed12_path, 'w') as output_bed12_file:
        # Write the track line at the top of the file
        output_bed12_file.write(f"track name={args.track_name} itemRgb=On\n")

        for line in bed_file:
            # Split the BED line into columns
            columns = line.strip().split('\t')

            # Get the abundance information from the name column
            name_parts = columns[3].split('|')
            peptide = name_parts[0]
            abundance = int(name_parts[-1])

            # Update the maximum abundance for the peptide
            max_abundance_dict[peptide] = max(max_abundance_dict.get(peptide, 0), abundance)

        # Rewind the bed_file to the beginning
        bed_file.seek(0)

        for line in bed_file:
            # Split the BED line into columns
            columns = line.strip().split('\t')

            # Get the abundance information from the name column
            name_parts = columns[3].split('|')
            peptide = name_parts[0]
            abundance = int(name_parts[-1])

            # Determine if the peptide is major or minor based on the relative abundance
            relative_abundance = abundance / max_abundance_dict[peptide]
            is_major = relative_abundance >= 0.5  # Adjust the threshold as needed

            # Set the RGB color based on the isoform type
            rgb_color = major_color if is_major else minor_color

            # Update the RGB color column in the BED line
            columns[8] = rgb_color

            # Convert the BED line to BED12 format
            bed12_columns = columns[:6] + [columns[6], columns[7], columns[8]] + columns[9:]

            # Write the updated BED12 line to the output file
            output_bed12_file.write('\t'.join(bed12_columns) + '\n')

    print("RGB colors added, BED file converted to BED12 format, and track line added.")

if __name__ == "__main__":
    main()
