# TXT to CSV Converter

A simple Python script that converts text files to CSV format.

## How it Works

The script automatically:
1. Reads all `.txt` files from the `input` directory
2. Converts each file to CSV format
3. Saves the converted files in the `output` directory with timestamps

## Usage

1. Place your `.txt` files in the `input` directory
2. Run the script:
   ```bash
   python script.py
   ```
3. Find your converted files in the `output` directory

Each output file will be named in the format: `original-name_YYYYMMDD_HHMMSS.csv`

## Requirements

- Python
- pandas
