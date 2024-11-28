import os
import requests

def get_imdb_id(movie_title):

    # Your API key
    API_KEY = "YOUR API KEY"

    # OMDb API endpoint
    API_URL = "http://www.omdbapi.com/"

    # Parameters
    PARAMS = {'s': movie_title, 'apikey': API_KEY, 'r': 'json'}

    # Sending GET request
    response = requests.get(url=API_URL, params=PARAMS)

    # Extracting data in json format
    search_data = response.json()

    # Check if 'Search' is in the data, and it has at least one result
    if 'Search' in search_data and len(search_data['Search']) > 0:
        return search_data['Search'][0]['imdbID']
    else:
        print(f"No IMDb ID found for {movie_title}")
        return None


def get_synopsis(imdb_id):
    if imdb_id is None:
        return "No synopsis found"

    # Your actual API key
    API_KEY = "YOUR API KEY"

    # OMDb API endpoint
    API_URL = "http://www.omdbapi.com/"

    # Parameters
    PARAMS = {'i': imdb_id, 'apikey': API_KEY, 'plot': 'full', 'r': 'json'}

    # Sending GET request
    response = requests.get(url=API_URL, params=PARAMS)

    # Extracting data in json format
    data = response.json()

    # Check if 'Plot' is in the data before returning it
    if 'Plot' in data:
        return data['Plot']
    else:
        print(f"No synopsis found for IMDb ID {imdb_id}")
        return "No synopsis found"


def create_synopsis_files(directory):
    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(directory):
        # Exclude '!Torrents' and 'Featurettes' directories from search
        dirs[:] = [d for d in dirs if d not in ['!Torrents', 'Featurettes']]

        for folder in dirs:
            # Extract the movie title from the folder name
            movie_title = folder.rsplit(' ', 1)[0]

            # Get IMDb ID
            imdb_id = get_imdb_id(movie_title)

            # Get synopsis
            synopsis = get_synopsis(imdb_id)

            # Create or overwrite a txt file in each folder
            with open(os.path.join(root, folder, 'synopsis.txt'), 'w') as f:
                f.write(synopsis)


# Your movies directory (Replace "D:\\03 - Cinema\\Movies" with your actual movie dir.)
create_synopsis_files('D:\\03 - Cinema\\Movies')

