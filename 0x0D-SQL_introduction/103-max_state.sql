-- script that displays the max temperature of each state
-- cat 103-max_state.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT state, MAX(value) AS "max_temp" FROM temperatures GROUP BY state ORDER BY state ASC;
