import gzip
import json
import os
import sys
import multiprocessing
from time import time


def process_file(filename):
    print("Reading file", path + filename, "... ")
    with gzip.open(path + filename, "rt") as file:
        count = 0
        for line in filter(lambda l: l != "", map(str.strip, file.readlines())):
            try:
                json.loads(line)
                count += 1
            except json.JSONDecodeError:
                print("Ignoring malformed tweet", line, file=sys.stderr)
    print("File", path + filename, "had", count, "tweets")
    return count


if __name__ == "__main__":
    start_time = time()
    path = "olympics/"
    files = os.listdir(path)
    n_files = len(files)
    print(n_files, "compressed files.")
    n_read_files = 16
    cpu_count = os.cpu_count()

    with multiprocessing.Pool(cpu_count) as pool:
        tweet_count = pool.map(process_file, files[:n_read_files])

    print("Total # of tweets:", sum(tweet_count))
    print("Elapsed time:", time() - start_time, "seconds")
