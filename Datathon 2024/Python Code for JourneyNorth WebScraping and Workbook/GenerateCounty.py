from openai import OpenAI
client = OpenAI()
import pandas as pd
import time

# Function to get county from OpenAI API based on the city and state
def get_county(city, state):
    try:
        # Construct the message for OpenAI
        prompt = f"Answer only with the name of the county where the city of '{city}', {state}. Add nothing else."
        
        # Request completion from OpenAI API
        response = client.chat.completions.create(
            model="gpt-4",  # Correct model name (gpt-4)
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Extract county name from response correctly
        county_name = response.choices[0].message.content
        return county_name
    except Exception as e:
        print(f"Error fetching county for {city}, {state}: {e}")
        return None

# Load the scraped CSV file
for year in range(1997, 2023):
    df = pd.read_csv(f'monarch_sightings_fall_{year}.csv')

    # Assume the CSV has columns for 'Town' and 'State/Province' (modify according to your actual CSV structure)
    if 'Town' in df.columns and 'State/Province' in df.columns:
        # Initialize a new column 'County' with empty values
        df['County'] = ''

        # Loop through each row and get the county for each city, state combination
        for index, row in df.iterrows():
            city = row['Town']
            state = row['State/Province']
            county = get_county(city, state)
            
            # Update the DataFrame with the fetched county
            df.at[index, 'County'] = county

            # Pause to respect OpenAI's rate limits
            usleep = lambda x: time.sleep(x/1000000.0)
            usleep(101) #sleep during 100μs
            if(index % 1000 == 0 and index != 0):
                print("x")

        # Save the updated DataFrame back to a new CSV
        df.to_csv(f'monarch_sightings_with_counties_{year}.csv', index=False)

        print(f"CSV file for year {year} updated with counties.")
    else:
        print("The necessary columns 'Town' and 'State/Province' were not found in the CSV file.")
