# colocacoesScraper
Web scraper for the national higher education access results

Built using selenium. Goes to the [official website](https://www.dges.gov.pt/coloc/2020/col1listas.asp) and does a depth-first traversal of every institution and course. Outputs names to a csv file.
Edit line 18 (`url_dict`) and insert the name of the file you want for output as key, and the root website (must be for either politechnical or university placements) and just run like a normal python program with `py .\colocacoes_scraper.py`
