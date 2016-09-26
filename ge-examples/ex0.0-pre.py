import os
import gzip
import json

if __name__ == "__main__":

    l = ["Python", "Ruby", "Scala", "Java", "Erlang", "Elixir", "Lisp"]
    print(sorted(l))

    data_path = "olympics/"
    files = os.listdir(data_path)
    for file in files:
        print(data_path + file)

    with open("olympics-uc/2016-08-14-00", "r") as f:
        for line in f.readlines():
            print(line)
            break

    with gzip.open("olympics/2016-08-14-00.gz", "rt") as f:
        for line in f.readlines():
            print(line)
            tweet_json = line
            break

    some_json = '{"withheld_copyright": true}'
    parsed_json = json.loads(some_json)
    print(parsed_json)
    parsed_json = json.loads(tweet_json)
    print(parsed_json)

    with open("tmp/test.json", "w") as f:
        json.dump(some_json, sort_keys=True, indent=4, fp=f)
