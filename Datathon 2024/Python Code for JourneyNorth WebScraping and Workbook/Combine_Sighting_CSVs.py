import pandas as pd
import glob

# Specify the path where the CSV files are located
# Update the path to where your CSV files are stored
path = "c:/Users/berbr/Documents/CommandLineGPT/"  # Make sure to include the trailing slash
all_files = glob.glob(path + "updated_*.csv")  # Adjust the pattern as needed

# Initialize an empty list to hold the DataFrames
dataframes = []

# Loop through the files and read them into DataFrames
for filename in all_files:
    df = pd.read_csv(filename)  # Read each CSV file into a DataFrame
    dataframes.append(df)        # Append the DataFrame to the list

# Combine all DataFrames into one
combined_df = pd.concat(dataframes, ignore_index=True)  # Preserve all observations

# Export the combined DataFrame to a new CSV file
combined_df.to_csv("monarch_sightings_fall_allyears.csv", index=False)
print("Combined CSV file has been created successfully.")
