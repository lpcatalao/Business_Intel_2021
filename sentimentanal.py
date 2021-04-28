import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA


sia = SIA()

results = []

for line in headlines:
    pol_score = sia.polarity_scores(line)
    pol_score['headline'] = line
    results.append(pol_score)

texto="Lost Passwords Lock Millionaires Out of Their Bitcoin Fortunes"
pol_score = sia.polarity_scores(texto)
print(pol_score)
##print(results[:3], width=100)