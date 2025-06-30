-- a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

SELECT tv_show.title, tv_show_generes.genere_id
FROM tv_show
JOIN tv_show_generes ON tv_show.id = tv_show_generes.genere_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;