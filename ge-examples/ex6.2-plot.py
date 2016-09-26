import matplotlib.pyplot as plt
import gzip
import json
from time import time
from etime import print_elapsed_time

if __name__ == "__main__":
    start_time = time()
    with gzip.open("results/replies_to.1442.json.gz", "rt") as f:
        replies_to_list = json.load(f)
        print(list(filter(lambda r: r[0] == "generalelectric", replies_to_list)))

        max_bars = 30
        replies_to_list = replies_to_list[:max_bars]
        print(replies_to_list)

        screen_names = list(reversed(list(map(lambda x: x[0], replies_to_list))))
        print(screen_names)
        positions = range(len(screen_names))
        count = list(reversed(list(map(lambda x: x[1], replies_to_list))))
        print(count)

        plt.barh(positions, count, align='center', alpha=0.4)
        plt.yticks(positions, screen_names)
        plt.xlabel('# of replies')
        plt.title("Users with more replies")

        print_elapsed_time(start_time, time())
        plt.show()
