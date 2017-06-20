Please download newsdata.sql

The database file cannot upload to Github due to the file size.

* View for total_views

```CREATE VIEW total_views
AS SELECT articles.title, author, count(*) AS views
FROM articles JOIN log
ON articles.slug = (regexp_split_to_array(path, E'/article/'))[2]
WHERE path != '/'
GROUP BY articles.title, author
ORDER BY views DESC;
```

* View for authors_total_views

```CREATE VIEW authors_total_views
AS SELECT authors.name, sum(views) AS totals_views
FROM total_views JOIN authors
ON total_views.author = authors.id
GROUP BY authors.name
ORDER BY total_views DESC;
```

* View for daily_view

```CREATE VIEW daily_view
AS SELECT COUNT(status) AS views, EXTRACT(month FROM time) AS month,
EXTRACT(day FROM time) AS date
FROM log
GROUP BY month, date;
```

* View for errors

```CREATE VIEW errors
AS SELECT COUNT(*) AS errors, EXTRACT(day FROM time) AS date
FROM log
WHERE status = '404 NOT FOUND'
GROUP BY date
ORDER BY date;
```

* View for error_percentage

```CREATE VIEW error_percentage
AS SELECT daily_view.month, daily_view.date,
ROUND((errors.errors * 100.0)/(daily_view.views), 2) AS error_percentage
FROM daily_view JOIN errors
ON daily_view.date = errors.date;
```
