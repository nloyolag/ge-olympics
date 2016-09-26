import gzip
import json
import os
import sys
import multiprocessing
from functools import reduce, partial
from time import time
from etime import print_elapsed_time


def get_tweets(lines):
    for line in lines:
        try:
            tweet = json.loads(line)
            yield tweet
        except json.JSONDecodeError:
            print("Ignoring malformed tweet", line, file=sys.stderr)


def process_tweets_file(tweet_map_function, reduce_function, reduce_init, filename):
    print("Reading file", filename)
    with gzip.open(filename, "rt") as file:
        map_result = []
        lines = filter(lambda l: l != "", map(str.strip, file.readlines()))
        for tweet in get_tweets(lines):
            map_result.append(tweet_map_function(tweet))
    return reduce(reduce_function, map_result, reduce_init)


def extract_lang(tweet):
    return tweet["lang"]


def count_langs(lang_dict, lang):
    if lang in lang_dict.keys():
        lang_dict[lang] += 1
    else:
        lang_dict[lang] = 1
    return lang_dict


def consolidate_count_langs(lang_dict_acc, lang_dict):
    for lang in lang_dict.keys():
        if lang in lang_dict_acc.keys():
            lang_dict_acc[lang] += lang_dict[lang]
        else:
            lang_dict_acc[lang] = lang_dict[lang]
    return lang_dict_acc


if __name__ == "__main__":
    start_time = time()
    data_path = "olympics/"
    files = sorted(os.listdir(data_path))
    n_files = len(files)
    print(n_files, "compressed files.")
    n_read_files = 1
    absolute_paths = list(map(lambda fp: data_path + fp, files))

    file_map_function = partial(process_tweets_file, extract_lang, count_langs, {})

    with multiprocessing.Pool() as pool:
        tweet_langs_per_file = pool.map(file_map_function, absolute_paths[:n_read_files])
        print(tweet_langs_per_file)

    tweet_langs = reduce(consolidate_count_langs, tweet_langs_per_file, {})
    print(tweet_langs)

    with gzip.open("results/langs." + str(n_read_files) + ".json.gz", "wt") as f:
        json.dump(tweet_langs, fp=f)

    print("Total # of languages:", len(tweet_langs))
    print_elapsed_time(start_time, time())
