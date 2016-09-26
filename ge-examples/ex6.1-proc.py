import gzip
import json
from time import time
from etime import print_elapsed_time
from proctweet import process_tweets, get_absolute_paths


def filter_is_reply(tweet):
    satisfy = False
    in_reply_to = tweet["in_reply_to_screen_name"]
    if in_reply_to is not None:
        satisfy = True
    return satisfy


def no_filter(tweet):
    return True


def extract_in_reply_to(tweet):
    in_reply_to = "None"
    if tweet["in_reply_to_screen_name"] is not None:
        in_reply_to = tweet["in_reply_to_screen_name"]
    return in_reply_to


def count_elements(element_dict, element):
    if element in element_dict.keys():
        element_dict[element] += 1
    else:
        element_dict[element] = 1
    return element_dict


def consolidate_counts(count_dict_acc, element_dict):
    for element in element_dict.keys():
        if element in count_dict_acc.keys():
            count_dict_acc[element] += element_dict[element]
        else:
            count_dict_acc[element] = element_dict[element]
    return count_dict_acc


def sort_listify(count_dict):
    keys = list(count_dict.keys())
    values = [count_dict[key] for key in keys]
    key_value_list = list(sorted(zip(keys, values), key=lambda x: x[1], reverse=True))
    return key_value_list


if __name__ == "__main__":
    start_time = time()
    n_read_files = 16
    absolute_paths = get_absolute_paths("olympics/", n_read_files)

    replies_to = process_tweets(filter_is_reply, extract_in_reply_to, count_elements, {}, consolidate_counts, {},
                                absolute_paths)
    print(replies_to)

    key_value_list = sort_listify(replies_to)
    print(key_value_list)

    with gzip.open("results/replies_to." + str(n_read_files) + ".json.gz", "wt") as f:
        json.dump(key_value_list, fp=f)

    print("Total # of users with replies:", len(replies_to))
    print_elapsed_time(start_time, time())
