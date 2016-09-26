import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import math

mu = 736147
sigma = 1
tweet_dates = mu + sigma * np.random.randn(10000)

minutes_per_day = 24 * 60
min_minute = math.floor(min(tweet_dates) * minutes_per_day)
max_minute = math.ceil(max(tweet_dates) * minutes_per_day)
min_time = min_minute / minutes_per_day
max_time = max_minute / minutes_per_day
print("Start time:", mdates.num2date(min_time), min_time)
print("End time:", mdates.num2date(max_time), max_time)
n_minutes = max_minute - min_minute
print("Minutes range size:", n_minutes)

fig = plt.figure()
ax = fig.add_subplot(111)

# the histogram of the data
n, bins, patches = ax.hist(tweet_dates, 50, facecolor='green', alpha=0.75, histtype="step", range=(min_time, max_time))
print(n)
print(bins)
print(patches)

plt.xticks(rotation="vertical")
ax.xaxis.set_major_locator(mdates.DayLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))  # %m-%d %H:%M  #%m-%d

ax.set_xlabel('Date')
ax.set_ylabel('Tweets per second')
ax.grid(True)

plt.show()
