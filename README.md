# 🎬 Netflix Movie Trend Analytics & Recommender
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://movie-trend-analytics.streamlit.app/)
**A full-stack data science project analyzing Netflix content trends and recommending movies.**

## 📌 Overview
This project performs Exploratory Data Analysis (EDA) on the Netflix dataset to uncover content trends, manages data using SQLite, visualizes insights via Power BI, and implements a Content-Based Movie Recommender System using Machine Learning (TF-IDF & Cosine Similarity).

The final output includes an interactive **Streamlit Web App** and a **Power BI Dashboard**.

---

## 🚀 Features
* **Data Cleaning:** Handled missing values and enriched the dataset (`data/cleaned_netflix.csv`).
* **EDA:** In-depth analysis of Genres, Directors, and Yearly Trends (`notebooks/01_data_cleaning_and_EDA.ipynb`).
* **SQL Integration:** Migrated data to a local SQLite database for structured querying.
* **Recommendation Engine:** Suggests similar movies based on plot, genre, and cast using NLP techniques.
* **Visualizations:**
    * **Power BI:** Interactive dashboard (`dashboard/movie_dashboard.pbix`).
    * **Streamlit:** Web-based data exploration and recommender interface.

---

## 📂 Folder Structure
```text
movie-trend-analytics/
├── data/
│   ├── netflix_titles.csv       # Raw Data
│   └── cleaned_netflix.csv      # Processed Data
├── notebooks/
│   └── 01_data_cleaning_and_EDA.ipynb
├── src/
│   ├── app.py                   # Streamlit Application
│   └── recommender.py           # ML Logic
├── sql/
│   └── load_csv_to_sqlite.py    # Database script
├── dashboard/
│   └── movie_dashboard.pbix     # Power BI File
├── requirements.txt             # Python Dependencies
└── README.md

```
## 🛠 Tech Stack
* **Language:** Python 3.10+
* **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
* **Web Framework:** Streamlit
* **Database:** SQLite
* **BI Tool:** Microsoft Power BI
```

---

## ⚙️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/mritunjay-18/movie-trend-analytics.git
cd movie-trend-analytics
```

### 2. Create Virtual Environment & Install Dependencies

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```


### 3. Run the Streamlit App
```bash
streamlit run src/app.py
```
**The app will open in your browser at http://localhost:8501**

## 📊 SQL Setup
To create the local database from the CSV file, run:

```bash
python sql/load_csv_to_sqlite.py
```

**This creates movie_data.db. You can now run SQL queries using Python or open the file in "DB Browser for SQLite".**

## 📝 Notes & Credits
* **Dataset:** Netflix Movies and TV Shows (Kaggle)
* **Author:** Mritunjay Rai
