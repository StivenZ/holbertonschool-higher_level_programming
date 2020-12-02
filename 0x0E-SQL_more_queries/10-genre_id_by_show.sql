-- list tv shows by genres ID
SELECT tv_shows.title, tv_shows_genres.genres_id FROM tv_shows JOIN tv_shows_genres WHERE tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id;
