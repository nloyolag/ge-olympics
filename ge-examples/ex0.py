import gzip
import json
import os
import sys
from time import time

if __name__ == "__main__":
    start_time = time()
    data_path = "olympics/"
    files = sorted(os.listdir(data_path))
    n_files = len(files)
    print(n_files, "compressed files.")
    n_read_files = 1
    tweet_count = []
    for file, j in zip(files[:n_read_files], range(n_read_files)):
        print("Reading file", str(j + 1) + "/" + str(n_files), data_path + file, end="... ")
        with gzip.open(data_path + file, "rt") as f:
            i = 0
            for line in f.readlines():
                line = line.strip()
                if line != "":
                    try:
                        tweet = json.loads(line)
                        i += 1
                    except json.JSONDecodeError:
                        print("Ignoring malformed tweet", line, file=sys.stderr)
        print(i, "tweets")
        tweet_count.append(i)

    print("Total # of tweets:", sum(tweet_count))
    print("Elapsed time:", time() - start_time, "seconds")
