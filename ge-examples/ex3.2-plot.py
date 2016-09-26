import gzip
import json
import math
from time import time
import matplotlib.pyplot as plt
from etime import print_elapsed_time

if __name__ == "__main__":
    start_time = time()
    with gzip.open("results/langs.1.json.gz", "rt") as f:
        tweet_langs = json.load(f)
        del tweet_langs["en"]
        del tweet_langs["und"]
        labels = list(tweet_langs.keys())
        counts = list(map(lambda lang: tweet_langs[lang], labels))
        explode = list(map(lambda lang: 0.1, labels))

        print("Labels:", labels)
        print("Counts:", counts)

        plt.pie(counts, labels=labels, explode=explode, autopct='%1.1f%%')
        plt.axis('equal')

        print_elapsed_time(start_time, time())
        plt.show()
