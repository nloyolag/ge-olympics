import gzip
import json
from functools import partial
from time import time
from etime import print_elapsed_time
from proctweet import process_tweets, get_absolute_paths


def filter_lang(target_lang, tweet):
    satisfy = False
    if tweet["lang"] is not None:
        satisfy = (tweet["lang"] == target_lang)
    return satisfy


def extract_country(tweet):
    country = "None"
    place = tweet["place"]
    if place is not None:
        country = place["country_code"]
    return country


def count_elements(element_dict, element):
    if element in element_dict.keys():
        element_dict[element] += 1
    else:
        element_dict[element] = 1
    return element_dict


def consolidate_counts(count_dict_acc, element_dict):
    for lang in element_dict.keys():
        if lang in count_dict_acc.keys():
            count_dict_acc[lang] += element_dict[lang]
        else:
            count_dict_acc[lang] = element_dict[lang]
    return count_dict_acc


if __name__ == "__main__":
    start_time = time()
    n_read_files = 1442
    absolute_paths = get_absolute_paths("olympics/", n_read_files)

    lang = "en"
    filter_lang_eng = partial(filter_lang, lang)

    lang_countries = process_tweets(filter_lang_eng, extract_country, count_elements, {}, consolidate_counts, {},
                                    absolute_paths)

    ensemble = {"lang": lang, "lang_countries": lang_countries}
    print(ensemble)
    with gzip.open("results/lang_countries." + str(n_read_files) + ".json.gz", "wt") as f:
        json.dump(ensemble, fp=f)

    print("Total # of countries:", len(lang_countries))
    print_elapsed_time(start_time, time())
