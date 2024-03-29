-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT tv_genres.name AS "genre", count(*) AS "number_of_shows"
FROM tv_show_genres
LEFT JOIN tv_genres ON tv_genres.id = genre_id GROUP BY genre_id ORDER BY count(*) DESC;
