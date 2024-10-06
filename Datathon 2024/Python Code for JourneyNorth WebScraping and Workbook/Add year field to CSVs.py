import pandas as pd
import os

# Function to add year field to the CSV file
def add_year_to_csv(file_path):
    # Extract the year from the filename
    filename = os.path.basename(file_path)
    
    # The year is the last part of the filename, split by underscores
    year = filename.split('_')[-1].split('.')[0]  # Extract year from 'monarch_sightings_fall_year.csv'

    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Add a new column 'Year' with the extracted year
    df['Year'] = year

    # Define the output filename
    output_file_path = os.path.join(os.path.dirname(file_path), f"updated_{filename}")

    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_file_path, index=False)

    print(f"Updated CSV file saved as: {output_file_path}")

# Main function to process CSV files for each year
if __name__ == "__main__":
    # Loop through each year from 1997 to 2022
    for year in range(1997, 2023):
        # Construct the file path for each year's CSV file
        file_path = f"c:/Users/berbr/Documents/CommandLineGPT/monarch_sightings_fall_{year}.csv"  # Adjust the path as needed
        
        # Check if the file exists before trying to add a year
        if os.path.exists(file_path):
            add_year_to_csv(file_path)
        else:
            print(f"File not found: {file_path}")
