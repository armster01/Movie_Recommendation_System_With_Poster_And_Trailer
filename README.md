# Movie_Recommendation_System_Advanced

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [How It Works](#how-it-works)

## Introduction
The Movie Recommendation System is a web application built with Streamlit that recommends movies based on user input. By leveraging machine learning techniques and movie metadata, users can receive personalized movie suggestions, complete with posters and trailer links.

## Features
- **Movie Recommendations**: Get personalized movie suggestions based on your favorite movies.
- **Movie Posters**: Displays posters of the recommended movies.
- **Trailer Links**: Provides direct links to the trailers of recommended movies.
- **Multi-Platform Links**: Fetches streaming links for Amazon Prime and Netflix (or any other platforms you want to include).

## Technologies Used
- **Python**: The main programming language for the project.
- **Streamlit**: A framework to create web apps quickly.
- **Pandas**: For data manipulation and analysis.
- **Pickle**: For loading machine learning models and data.
- **Requests**: To fetch data from APIs.
- **TMDB API**: Used for movie metadata, including movie posters.

## Setup Instructions
To set up the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/armster01/Movie_Recommendation_System_Advanced.git
   cd Movie_Recommendation_System_Advanced

2. **Install Dependencies: Create a virtual environment (optional but recommended) and install the required packages**:
   pip install -r requirements.txt

3. **Run the App: Start the Streamlit app**:
   streamlit run app.py

## Usage
1. Open the app in your web browser.
2. Select a movie from the dropdown menu.
3. Click the "Recommend" button to view movie suggestions, posters, and trailers.

## How It Works
1. The app uses a collaborative filtering or content-based filtering model to recommend movies based on user input.
2. Movie data is fetched from the TMDB API, including movie titles, posters, and other relevant information.
3. The recommended movies are displayed along with their posters and links to trailers.

## Contributing
Contributions are welcome! If you'd like to contribute to the project, please fork the repository and submit a pull request.

Fork the repo.
1. Create your feature branch (git checkout -b feature/AmazingFeature).
2. Commit your changes (git commit -m 'Add some AmazingFeature').
3. Push to the branch (git push origin feature/AmazingFeature).
4. Open a pull request.
