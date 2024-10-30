import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=bea536250f8c05f19774a87662b0c4f3&language=en-US'.format(movie_id))
    data = response.json()

    #Check if 'poster path' exist, if not, return a default placeholder
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        # Return a default image URL or handle the absence of a poster as you prefer
        return "https://via.placeholder.com/500x750?text=No+Image+Available"

def fetch_trailer_link(movie_name):
    # Generate a YouTube search link
    search_query = movie_name + " trailer"
    return f"https://www.youtube.com/results?search_query={search_query.replace(' ', '+')}"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    trailer_links = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))
        # fetch YouTube Link
        trailer_links.append(fetch_trailer_link(movies.iloc[i[0]].title))

    return recommended_movies,recommended_movies_poster,trailer_links

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommendation System')

st.markdown("<h4 style='font-size:24px;'>Tell the movie name</h4>", unsafe_allow_html=True)
selected_movie_name = st.selectbox("", movies['title'].values)

if st.button('Recommend'):
    names,posters,trailer_links = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
        st.write(f"[Watch Trailer]({trailer_links[0]})")

    with col2:
        st.text(names[1])
        st.image(posters[1])
        st.write(f"[Watch Trailer]({trailer_links[1]})")

    with col3:
        st.text(names[2])
        st.image(posters[2])
        st.write(f"[Watch Trailer]({trailer_links[2]})")

    with col4:
        st.text(names[3])
        st.image(posters[3])
        st.write(f"[Watch Trailer]({trailer_links[3]})")

    with col5:
        st.text(names[4])
        st.image(posters[4])
        st.write(f"[Watch Trailer]({trailer_links[4]})")