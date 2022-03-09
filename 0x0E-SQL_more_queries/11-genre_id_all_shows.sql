--lists all shows contained in the database
SELECT tv_shows.title, 
CASE ISNUMERIC(tv_show_genres.genre_id)  THEN tv_show_genres.genre_id
ELSE Null
END
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
