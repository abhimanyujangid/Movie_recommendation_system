import streamlit as st
import pickle
import pandas as pd


def recommend (movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True , key = lambda x:x[1])[1:7]
    recommemded_movies = []
    for i in movies_list:
        movie_id = i[0]
        # fetch poster from API

        recommemded_movies.append(movies.iloc[i[0]].title)
    return recommemded_movies


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity =  pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
select_movie_name = st.selectbox('How would you like to be contacted?',(movies['title'].values))
# create button
if st.button('Recommend'):
    recommendation = recommend(select_movie_name)
    for i in recommendation:
        st.write(i)

