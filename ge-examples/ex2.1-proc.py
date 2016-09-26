import gzip
import json
import os
import sys
import multiprocessing
import operator
import functools
from time import time
import matplotlib.dates as mdates
from etime import print_elapsed_time


def process_tweets_file(tweet_map_function, filename):
    print("Reading file", filename, "... ")
    result = []
    with gzip.open(filename, "rt") as file:
        for line in filter(lambda l: l != "", map(str.strip, file.readlines())):
            try:
                tweet = json.loads(line)
                result.append(tweet_map_function(tweet))
            except json.JSONDecodeError:
                print("Ignoring malformed tweet", line, file=sys.stderr)
    print("File", filename, "had", len(result), "tweets")
    return result


def extract_timestamp(tweet):
    return mdates.datestr2num(tweet["created_at"])


if __name__ == "__main__":
    start_time = time()
    data_path = "olympics/"
    files = sorted(os.listdir(data_path))
    n_files = len(files)
    print(n_files, "compressed files.")
    n_read_files = 16
    absolute_paths = list(map(lambda fp: data_path + fp, files))

    file_map_function = functools.partial(process_tweets_file, extract_timestamp)

    with multiprocessing.Pool() as pool:
        tweet_dates_per_file = pool.map(file_map_function, absolute_paths[:n_read_files])

    tweet_dates = functools.reduce(operator.add, tweet_dates_per_file)

    with gzip.open("results/timestamps.json." + str(n_read_files) + ".gz", "wt") as f:
        print(tweet_dates, file=f)

    print("Total # of tweets:", len(tweet_dates))
    print_elapsed_time(start_time, time())
