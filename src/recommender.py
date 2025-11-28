import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "..", "data", "cleaned_netflix.csv")

df = pd.read_csv(csv_path)

df['combined'] = df['title'] + " " + df['listed_in'] + " " + df['description']

tfidf = TfidfVectorizer(stop_words='english')
matrix = tfidf.fit_transform(df['combined'])

similarity = cosine_similarity(matrix)

def recommend(title):
    title = title.lower()
    if title not in df['title'].str.lower().values:
        return ["Movie not found"]

    idx = df[df['title'].str.lower() == title].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]

    return df.iloc[[i[0] for i in scores]]['title'].to_list()