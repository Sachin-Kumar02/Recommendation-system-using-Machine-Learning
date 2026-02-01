import streamlit as st
import pandas as pd


ndf = pd.read_csv("cleaned.csv",usecols=['title'])

st.title('MOVIE RECOMMENDER SYSTEM')
movie_exp= ['Guardians of the Galaxy','Interstellar','Mad Max: Fury Road','Minions','Deadpool']

st.header("Top movies")
c1 ,c2 , c3 , c4 ,c5 = st.columns(5)
c1.write(movie_exp[0])
c2.write(movie_exp[1])
c3.write(movie_exp[2])
c4.write(movie_exp[3])
c5.write(movie_exp[4])
st.subheader("")
movie = st.text_input('ENTER MOVIE NAME')

similarity1 = pd.read_csv('similarity' ,index_col=0)
similarity1 = similarity1.to_numpy()

#####################

def recommend(movie):
    try:
        movie = movie.lower()
        movie_index = ndf[ndf['title'] == movie].index[0]
        distances = similarity1[movie_index]
        top_5 = sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]
        
        dict = {}
        for i,j in top_5:
            dict[str(ndf.iloc[i].title).upper()] = str(round(j,2))
        
        st.dataframe(dict)
    except:
        print("given movies is not in list")
        

#########################
if st.button('Recommend'):
    st.header('Similar movies')
    recommend(movie)
    

