# Zuerst muessen wir Twython importieren.
from twython import Twython, TwythonError

# Authentifizierung mit Twitter. Twitter API credentials. Sind auf der Twitter Developer Seite zu finden, wo ihr Euren Account gemacht habt.
twitter = Twython('JvNDePaaARglxs5MuGgEYJjkv', 'saT7WTmJddLijZ8fsCsev1loWkoTXUfIj7wXvqCD43rFABfuwN')
# Starte die Twittersuche nach @borussia
search_results = twitter.search(q='@realDonaldTrump ‏', count=1000)
# Speichere die Ergebnisse in das Dictionary all_tweets
all_tweets = search_results['statuses']
# Ausgabe des Dictionaries in einer Schleife
for tweet in all_tweets:
    print (tweet['text'])
    print ("\n")
<<<<<<< HEAD


#test_gitkraken & github
#Hoi zäme :) Was macheder so? 
#blablabla
=======
<<<<<<< Updated upstream

HALLOOOOO


#test_gitkraken & github
<<<<<<< Updated upstream
=======
Hallo from Calebe
Test Calebe
>>>>>>> Stashed changes
>>>>>>> master
