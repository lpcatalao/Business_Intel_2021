import requests
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import time
import ciso8601
from csv import DictWriter


sia = SIA()
articles=[]

for i in range (101):
    resp = requests.get(f"https://api.nytimes.com/svc/search/v2/articlesearch.json?q=bitcoin&api-key=noaYtZjAx9IAkUMH4vjyZUCzfUV66o1i&page={i}")

    print(f"now reading page number {i}")

    for article in resp.json()["response"]["docs"]:
        date = article["pub_date"]
        dateseconds= ciso8601.parse_datetime(date)
        dateseconds = time.mktime(dateseconds.timetuple())
        main = article["headline"]["main"]
        pol_score = sia.polarity_scores(main)
        main_score=pol_score["compound"]
        articles.append({"timestamp" : dateseconds, "title" : main, "score" : main_score})

    time.sleep(7)

with open("news.csv", "w") as outfile:
    writer = DictWriter(outfile, ('timestamp', 'title', 'score'))
    writer.writeheader()
    writer.writerows(articles)


