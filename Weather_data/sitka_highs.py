from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_raw = next(reader)

# Check coulmn header and their index
# for index, coulmn_header in enumerate(header_raw):
#     print(index, coulmn_header)

# Extract high temparature; it's contain in coulmn 5, index 4
highs, dates = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    highs.append(high)
    dates.append(current_date)


# Plot the high temparature
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')

# Format plot
ax.set_title("Daily High Temparatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("Temparature(F)", fontsize=14)
ax.tick_params(labelsize=14, labelrotation=45)

plt.show()

