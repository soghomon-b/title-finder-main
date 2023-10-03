#!/bin/bash

# Input and output file names
input_file="C:\Users\soghm\OneDrive\Desktop\title-finder-main\title finder\line_skipping\test.txt"
output_file="C:\Users\soghm\OneDrive\Desktop\title-finder-main\title finder\line_skipping\test.pdf"

# Check if the input file exists
if [ ! -f "$input_file" ]; then
  echo "Input file '$input_file' does not exist."
  exit 1
fi

# Create a temporary file with empty lines between each line
temp_file="temp.txt"
awk '{print $0 "\n"}' "$input_file" > "$temp_file"

# Convert the temporary file to PDF using Pandoc
pandoc "$temp_file" -o "$output_file"

# Clean up the temporary file
rm "$temp_file"

echo "Conversion complete. Output PDF saved as '$output_file'."
