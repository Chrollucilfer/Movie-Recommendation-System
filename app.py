import streamlit as st
import pandas as pd
import pickle

movies_lists = pickle.load(open('C:\\Users\\karta\\PycharmProjects\\pythonProject2\\movies.pkl', 'rb'))
# movies_lists = movies_lists['title'].values
st.title('Movie Recommendation System')
similarity = pickle.load(open('C:\\Users\\karta\\PycharmProjects\\pythonProject2\\similarity.pkl', 'rb'))
def recommend(movie):
  movie_index=movies_lists[movies_lists['title']==movie].index[0]
  distances=similarity[movie_index]
  L=[]
  movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
  for i in movies_list:
    L.append(movies_lists.iloc[i[0]].title)
  return L

option=st.selectbox(
    'Choose your movies',movies_lists['title'].values)

if st.button('Recommend'):
    recommendations=recommend(option)
    for i in recommendations:
        st.write(i)
