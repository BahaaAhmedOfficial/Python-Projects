# Movie Synopsis Creator

This Python script fetches movie synopses from the OMDb API and creates a synopsis file for each movie in a specified directory. It's designed to help you organize and manage your movie collection with automatically generated synopses.

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. **Clone the repository**:
    ```
    bash
    git clone https://github.com/yourusername/moviesynopsis.git
    cd moviesynopsis
    ```

2. **Install the required packages**:
    ```
    bash
    pip install requests
    ```

## Usage

1. **Update the `create_synopsis_files` function** in `main.py` to use your actual movies directory:
    ```
    python
    create_synopsis_files('D:\\03 - Cinema\\Movies')
    ```

2. **Run the script**:
    ```
    bash
    python main.py
    ```

## Functions

### `get_imdb_id(movie_title)`

Fetches the IMDb ID for the given movie title using the OMDb API.

- **Parameters**: `movie_title` (str) - The title of the movie.
- **Returns**: `imdb_id` (str) - The IMDb ID of the movie.

### `get_synopsis(imdb_id)`

Fetches the synopsis for the given IMDb ID using the OMDb API.

- **Parameters**: `imdb_id` (str) - The IMDb ID of the movie.
- **Returns**: `synopsis` (str) - The full plot synopsis of the movie.

### `create_synopsis_files(directory)`

Walks through all directories and subdirectories in the specified directory, fetches IMDb IDs and synopses for movies, and creates synopsis files.

- **Parameters**: `directory` (str) - The path to the directory containing movie folders.

## Notes

- Make sure to use your actual OMDb API key.
- Excludes the unwanted directories like my `!Torrents` and `Featurettes` directories from the search.


---

Happy movie watching! 🎬
