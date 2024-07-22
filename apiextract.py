import requests
import time
import pandas as pd
from datetime import datetime
pd.set_option('display.max_column',None)

api_key = '4eefc1a2e5e226c9176fb1fc2cd2a9d1'  # Replace 'your_api_key' with your actual TMDb API key
page_no= 5
url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=en-US&page={page_no}'

# query header

max_retries = 3
retry_delay = 5  # seconds
movies_data = []


for attempt in range(max_retries): #0,1,2
    try:
        # 0
        # Make the GET request
        
        response = requests.get(url)
        # print(1)
        # print(type(response)) <class 'requests.models.Response'>
        # print(2)
        # Check if the request was successful (status code 200)
        # 404 for not found
        
        response.raise_for_status()
        # print(1)
        # print(response.raise_for_status()) --> None
        # print(2)
        # Parse the JSON data in the response
        data = response.json()
        # print(1)
        # print(type(data)) --><class 'dict'>
        # print(2)
        # Check if there are any movies in the response
        # print(data)
        print(data['results'][0])
        if 'results' in data and len(data['results']) > 0:
            # Append the movie data to the list
            movies_data.extend(data['results'])
            break  # Break out of the loop if successful

        else:
            print("No movies found in the response.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

        # If it's not the last attempt, wait before retrying
        if attempt < max_retries - 1:
            print(f"Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
        else:
            print("Max retries reached. Exiting.")

# Create a DataFrame from the list of movie data
df = pd.DataFrame(movies_data)

# Display the DataFrame
# print(df)
# print(len(df.columns))
# print(df.columns)
df1=df[["adult","genre_ids","id","original_language","title","release_date","vote_count"]]
print(df1)
current_datetime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
path1 = f"/home/mukunthan/Documents/Personal/Learning/BigData/stock-poc/api_data_{page_no}_{current_datetime}.csv"
path2 = f"/home/mukunthan/Documents/Personal/Learning/BigData/stock-poc/snowflake_data_{page_no}_{current_datetime}.csv"

df.to_csv(path1, index=False)
df1.to_csv(path2, index=False)
print("Files Has been Written")



