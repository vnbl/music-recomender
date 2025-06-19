# Spotify Recommender

A data mining and recommendation system for Spotify artists, built with Python, Streamlit, Spotipy, and PySpark. This project allows users to search for artists, retrieve their genres and metadata, and perform data analysis on Spotify artist data.

## Project Structure

```
.env
.gitignore
README.md
analysis/
    .gitignore
    .python-version
    Dockerfile
    analysis/hello.py
    pyproject.toml
    README.md
    uv.lock
    data/
        raw/
            dataset.csv
    notebooks/
        exploratory_analysis.ipynb
        .ipynb_checkpoints/
            exploratory_analysis-checkpoint.ipynb
recommender/
    .python-version
    main.py
    mining.py
    output.csv
    pyproject.toml
    README.md
    utils.py
    uv.lock
```

## Features

- **Artist Genre Search:** Search for an artist and display their genres using a Streamlit web interface. *(In development)*
- **Spotify Data Mining:** Extract detailed artist metadata from Spotify using Spotipy and PySpark.
- **Data Analysis:** Analyze and visualize artist data in Jupyter notebooks. *(Working)*
- **Docker Support:** Run the analysis environment in a Docker container for reproducibility.

## Getting Started

### Prerequisites

- Python 3.8+
- [Spotify Developer Account](https://developer.spotify.com/)
- Docker (optional, for analysis environment)

### Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/spotify-recommender.git
    cd spotify-recommender
    ```

2. **Set up environment variables:**

    Create a `.env` file in the root directory with your Spotify API credentials:
    ```
    SPOTIPY_CLIENT_ID=your_client_id
    SPOTIPY_CLIENT_SECRET=your_client_secret
    ```

3. **Install dependencies:**

    For the recommender app:
    ```sh
    cd recommender
    pip install -r requirements.txt  # or use pyproject.toml/uv/poetry as appropriate
    ```

    For the analysis environment:
    ```sh
    cd ../analysis
    pip install -r requirements.txt  # or use pyproject.toml/uv/poetry as appropriate
    ```

### Running the Recommender App

> **Note:** The recommender app is under development and may not be fully functional.

1. **Start the Streamlit app:**
    ```sh
    cd recommender
    streamlit run main.py
    ```

2. **Usage:**
    - Enter an artist's name in the web interface to view their genres.

### Data Mining & Analysis

- Use `mining.py` to extract artist metadata and save it as a CSV.
- Explore and analyze the data in Jupyter notebooks under `analysis/notebooks`.

### Docker (for Analysis)

To run the analysis environment in Docker:
```sh
cd analysis
docker build -t spotify-analysis .
docker run -p 8888:8888 spotify-analysis
```
Access Jupyter at [http://localhost:8888](http://localhost:8888).

## File Overview

- `recommender/main.py`: Streamlit app for artist genre search. *(In development)*
- `recommender/mining.py`: Scripts for mining Spotify artist data.
- `analysis`: Data analysis environment and notebooks. *(Working)*
- `analysis/Dockerfile`: Docker setup for analysis.

## License

MIT License

## Acknowledgements

- [Spotipy](https://spotipy.readthedocs.io/)
- [Streamlit](https://streamlit.io/)
- [PySpark](https://spark.apache.org/docs/latest/api/python/)
- [Jupyter](https://jupyter.org/)