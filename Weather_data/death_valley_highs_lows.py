from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()
# print(lines)

reader = csv.reader(lines)
row_header = next(reader)

# for index, coulmn_header in enumerate(row_header):
#     print(index, coulmn_header)

# Extract data from csv coulmn
highs, lows, dates = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')

    try:
        high = int(row[3])
        low = int(row[4])
    except:
        print(f"Missing data from {current_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)

# Plot high, lows, and date values
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
ax.set_title("Death Valley Temparature - 2021", fontsize=20)
ax.set_xlabel("", fontsize=14)
ax.set_ylabel("Temparature(F)", fontsize=14)

plt.show()
