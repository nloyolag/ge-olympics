import gzip
import json
import math
from time import time
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from etime import print_elapsed_time

if __name__ == "__main__":
    start_time = time()
    minutes_per_day = 24 * 60
    with gzip.open("results/timestamps.json.1442.gz", "rt") as f:
        tweet_dates = json.load(f)
        min_minute = math.floor(min(tweet_dates) * minutes_per_day)
        max_minute = math.ceil(max(tweet_dates) * minutes_per_day)
        min_time = min_minute / minutes_per_day
        max_time = max_minute / minutes_per_day
        print("Start time:", mdates.num2date(min_time), min_time)
        print("End time:", mdates.num2date(max_time), max_time)
        n_minutes = max_minute - min_minute
        print("Minutes range size:", n_minutes)

        fig, ax = plt.subplots(1, 1)
        n, bins, patches = ax.hist(tweet_dates, bins=n_minutes, color='lightblue', histtype="step",
                                   range=(min_time, max_time))
        print(n)
        print(bins)
        print(patches)
        plt.xticks(rotation="vertical")
        ax.xaxis.set_major_locator(mdates.DayLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))  # %m-%d %H:%M  #%m-%d
        ax.set_ylabel("Tweets per minute")
        ax.set_title("Twitting rate throughout time")

        print_elapsed_time(start_time, time())
        plt.show()
