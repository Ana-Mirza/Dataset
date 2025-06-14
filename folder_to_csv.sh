#!/bin/bash

# Argument validation check
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <folder>"
    exit 1
fi

# last folder in path introduced must be named "log_data" !!!
# also, a folder named "csv_data" must exist in the same location as the log_data folder
folder=$1

# transform every log file in <folder> to a csv file 
for file in $(ls $folder); do python3 text_to_csv.py $folder/$file; done
