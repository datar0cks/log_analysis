# Log Analysis
This is a simple reporting tool that allows to get reports from the news logs.

# Reports supported
Currently following 3 reports are supported -
* 3 most popular articles of all times
* Most popular article authors of all times
* Days with more than 1 percent request error rate

# Pre-requisite
### Installation
Get code from [here](https://github.com/datar0cks/log_analysis.git)

### Database view creation
1. Connect to news database with `psql news`
2. Create the following view 
```
create view vw_article_summary as
select art.title, art.author, a.name, count(1) as views
from (select regexp_matches(path,'/article/([A-Za-z0-9\-]+)') slug 
      from log
	  where status like '200%'
      and   path != '/'
	  ) as l, 
      articles art, 
	  authors a
where l.slug[1] = art.slug
and   art.author = a.id
group by art.title, art.author, a.name
order by count(1) desc;
```

# How to pull the reports
Run `python log_analysis.py`
Follow instructions
Program will exit without any result if correct report number is not entered

## Assumptions
Current version of the implemented code assumes -
1. An article can be only written by a single author
2. "Most popular article author" - will not return authors with no articles (in case such data is uploaded)

