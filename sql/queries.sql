-- Top 5 Genres by Number of Movies
SELECT main_genre AS genre, COUNT(*) AS total
FROM movies
GROUP BY main_genre
ORDER BY total DESC
LIMIT 5;

-- Number of Movie Releases per Year
SELECT year_added, COUNT(*) AS total_releases
FROM movies
GROUP BY year_added
ORDER BY year_added;

-- Top 10 Directors by Number of Movies Directed
SELECT director, COUNT(*) AS cnt
FROM movies
GROUP BY director
ORDER BY cnt DESC
LIMIT 10;