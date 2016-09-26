import matplotlib.pyplot as plt
import gzip
import json
from time import time
from etime import print_elapsed_time
import pycountry


def get_country_name(country_code):
    return pycountry.countries.get(alpha2=country_code).name


if __name__ == "__main__":
    start_time = time()
    with gzip.open("results/lang_countries.16.json.gz", "rt") as f:
        ensemble = json.load(f)
        lang = pycountry.languages.get(iso639_1_code=ensemble["lang"]).name
        print("Language:", lang)
        lang_countries = ensemble["lang_countries"]
        print("Countries:", lang_countries)
        del lang_countries[""]
        del lang_countries["None"]
        # del lang_countries["US"]
        # del lang_countries["GB"]

        countries = list(lang_countries.keys())
        count = [lang_countries[key] for key in countries]

        max_bars = 40
        s_country_count = list(sorted(zip(countries, count), key=lambda x: x[1], reverse=True))[:max_bars]

        countries = list(reversed(list(map(lambda x: get_country_name(x[0]), s_country_count))))
        print(countries)
        positions = range(len(countries))
        count = list(reversed(list(map(lambda x: x[1], s_country_count))))
        print(count)

        plt.barh(positions, count, align='center', alpha=0.4)
        plt.yticks(positions, countries)
        plt.xlabel('# of tweets')
        plt.title("Countries where " + lang + " tweets came from")

        print_elapsed_time(start_time, time())
        plt.show()
