-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
-- cat 101-not_a_comedy.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT tv_shows.title
FROM tv_shows
WHERE id NOT IN (
  SELECT tv_show_genres.show_id
  FROM tv_genres
  JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
  WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title ASC;
