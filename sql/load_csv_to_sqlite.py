import sqlite3
import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "..", "data", "cleaned_netflix.csv")
db_path = os.path.join(current_dir, "..", "movie_data.db")

df = pd.read_csv(csv_path)

conn = sqlite3.connect(db_path)
df.to_sql("movies", conn, if_exists="replace", index=False)

print(f"Success! Database created at: {db_path}")
conn.close()