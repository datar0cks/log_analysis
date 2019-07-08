#!/usr/bin/python

DBNAME = "news"

report_list = {
      "1": ["MOST_POPULAR_ARTICLES", "Most popular articles", "views"],
      "2": ["MOST_POPULAR_AUTHORS", "Most popular authors", "views"],
      "3": ["ERROR_RATE_GT_1", "Days with >1% error rate", "errors"]
}

report_query = {
    "MOST_POPULAR_ARTICLES": """select title, views
                from vw_article_summary
                limit 3""",
    "MOST_POPULAR_AUTHORS": """select a.name, sum(views)
                from vw_article_summary a
                group by a.name
                order by sum(views) desc""",
    "ERROR_RATE_GT_1": """select dt, round(error_rate,2) as error_rate
                from
                  (select date(time) dt,
                          cast(count(case
                                       when status like '404%'
                                         then 1
                                         else null
                                     end) as decimal)/count(1) * 100
                                                           as error_rate
                   from log
                   group by date(time)
                  ) as t
               where error_rate > 1"""
}
