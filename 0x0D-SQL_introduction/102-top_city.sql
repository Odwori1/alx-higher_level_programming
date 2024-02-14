-- script that displays top 3 of cities temp during July and Augus
-- cat 102-top_city.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT city, AVG(value) AS "avg_temp" FROM temperatures WHERE month = 7 or month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
