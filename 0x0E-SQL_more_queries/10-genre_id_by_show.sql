-- list tv shows by genres ID
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows JOIN tv_show_genres WHERE tv_shows.id = tv_show_genres.show_id AND tv_shows.id <= 1;
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id;
