import os, sys
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from recommender import recommend

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "cleaned_netflix.csv")

df = pd.read_csv(DATA_PATH)

st.set_page_config(page_title="Netflix Trends", layout="wide")
st.title("🎬 Netflix Movie Trend Analytics & Recommender")

menu = ["Overview", "Visualizations", "Recommender", "SQL Results"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Overview":
    st.subheader("Dataset head")
    st.dataframe(df.head())
    st.write("Shape:", df.shape)
    st.write("Columns:", list(df.columns))

elif choice == "Visualizations":
    st.subheader("Movies vs TV Shows")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='type', ax=ax)
    st.pyplot(fig)

    st.subheader("Top 10 Genres")
    top_genres = df['main_genre'].value_counts().head(10)
    fig2, ax2 = plt.subplots(figsize=(8,5))
    sns.barplot(x=top_genres.values, y=top_genres.index, ax=ax2)
    st.pyplot(fig2)

    st.subheader("Yearly Trend")
    yearly = df['year_added'].value_counts().sort_index()
    fig3, ax3 = plt.subplots(figsize=(10,4))
    sns.lineplot(x=yearly.index, y=yearly.values, marker='o', ax=ax3)
    ax3.set_xlabel("Year Added")
    ax3.set_ylabel("Count")
    st.pyplot(fig3)

elif choice == "Recommender":
    st.subheader("Movie Recommender")
    movie = st.text_input("Enter movie title (exact or partial)")
    if st.button("Recommend"):
        if not movie.strip():
            st.warning("Enter a movie title first.")
        else:
            res = recommend(movie)
            st.write("Recommendations:")
            for r in res:
                st.write("- " + r)

elif choice == "SQL Results":
    st.subheader("Sample SQL Queries (Top genres)")
    # show top 10 genres as a table
    st.table(df['main_genre'].value_counts().head(10))