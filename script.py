import requests
import json

resp = requests.get("https://api.nytimes.com/svc/search/v2/articlesearch.json?q=bitcoin&api-key=noaYtZjAx9IAkUMH4vjyZUCzfUV66o1i&page=2")

article = resp.json()["response"]["docs"][0]
del article["multimedia"]
date = article["pub_date"]
main = article["headline"]["main"]
##subtitle = article["abstract"]
print(json.dumps(article, indent=4))