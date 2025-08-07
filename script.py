import os
import pandas as pd
from datetime import datetime
import glob

def convert_txt_to_csv():
    input_dir = 'input'
    output_dir = 'output'

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Get all .txt files in input folder
    txt_files = glob.glob(os.path.join(input_dir, "*.txt"))
    
    if not txt_files:
        print("No .txt files found in 'input' folder.")
        return

    for txt_file in txt_files:
        try:
            # Read the .txt file assuming it's comma-separated
            df = pd.read_csv(txt_file)

            # Generate timestamp for this file
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            
            # Create output filename: original_name_timestamp.csv
            base_name = os.path.splitext(os.path.basename(txt_file))[0]
            output_filename = f"{base_name}_{timestamp}.csv"
            output_path = os.path.join(output_dir, output_filename)

            # Save to CSV
            df.to_csv(output_path, index=False)
            print(f"✅ Converted '{txt_file}' to '{output_filename}'")

        except Exception as e:
            print(f"❌ Failed to process {txt_file}: {e}")

if __name__ == "__main__":
    convert_txt_to_csv()