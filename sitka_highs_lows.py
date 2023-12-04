from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path("weather_data/sitka_weather_2021_simple.csv")
lines = path.read_text().splitlines()


reader = csv.reader(lines) # This is a reader object which can be used to parse each line in the file
# When given a reader object, the next() function returns the next line
# in the file, starting from the beginning of the file. Since we call it only once here,
# it just returns the first line of the file, which contains the file headers.
header_row = next(reader) 

# To make it easier to understand the file header data, let’s print each header
#and its position in the list:

for index, column_header in enumerate(header_row):
    print(index, column_header)

""" Output:
0 STATION
1 NAME
2 DATE
3 TAVG
4 TMAX
5 TMIN
"""

# We now know that the data for the high and low temps is stored in
# columns 4 and 5 respectively

# Extract dates, highs and lows:
dates, highs, lows = [], [], []
for row in reader: # The reader object picks up from where it left off
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

print(highs)
print(lows)

# Plot the high temperatures

# plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red")
ax.plot(dates, lows, color="blue")
ax.set_title("Daily High and low Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() # turns dates diagonally so they don't overlap in img
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()