import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL
for year in range(1997, 2023):
    url = f"https://journeynorth.org/sightings/querylist.html?season=fall&map=monarch-adult-fall&year={year}&submit=View+Data"

    # Send a GET request to the website
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the table in the HTML
        table = soup.find('table')  # Modify if necessary depending on how the table is structured
        
        # Extract table rows
        rows = table.find_all('tr')
        
        # Extract the header (first row) and data (remaining rows)
        header = [th.text.strip() for th in rows[0].find_all('th')]
        data = []
        for row in rows[1:]:
            cols = [td.text.strip() for td in row.find_all('td')]
            data.append(cols)
        
        # Convert to pandas DataFrame
        df = pd.DataFrame(data, columns=header)
        
        # Display the DataFrame
        print(df)
        
        # Save the DataFrame to a CSV file
        df.to_csv(f'monarch_sightings_fall_{year}.csv', index=False)
        
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

