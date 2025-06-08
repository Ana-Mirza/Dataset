import csv
import re
import sys
import os

# Input and output file names
input_file = sys.argv[1]
output_file = input_file.replace('.log', '.csv').replace('log_data', 'csv_data')

# Open the input file and read the lines
with open(input_file, 'r') as f:
    lines = f.readlines()

# Prepare data
data = []

for line in lines:
    # Match lines like: [19] 472, 58, -1282
    match = re.match(r'\[(\d+)\]\s+([-]?\d+),\s+([-]?\d+),\s+([-]?\d+)', line)
    if match:
        timestamp, x, y, z = match.groups()
        data.append([timestamp, x, y, z])

print(input_file)
print(output_file)

# Write to CSV
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['timestamp', 'x', 'y', 'z'])
    writer.writerows(data)

print(f"Converted {len(data)} records to {output_file}")
