-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- cat 100-not_my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT tv_genres.name
FROM tv_genres
WHERE id NOT IN (
  SELECT tv_show_genres.genre_id
  FROM tv_shows
  JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
  WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name ASC;
