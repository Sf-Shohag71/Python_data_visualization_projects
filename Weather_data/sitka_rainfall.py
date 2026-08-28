from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

sitka_rainfall = Path('weather_data/sitka_weather_2021_full.csv')
lines = sitka_rainfall.read_text().splitlines()

reader = csv.reader(lines)
header = next(reader)

# Column header and their indices
# for index, col_header in enumerate(header):
#     print(index, col_header, end='')

# 0-STATION 1-NAME 2-DATE 3-AWND 4-PGTM 5-PRCP 6-TAVG 7-TMAX 8-TMIN 9-WDF210 WDF511 WSF212 WSF513 WT0114 WT0215 WT0416 WT0517 WT0818 WT09

rainfalls, dates, t_max, t_min = [], [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        rainfall = float(row[5])
        high = int(row[7])
        low = int(row[8])
    except:
        print(f"Missing information: {current_date}")
    else:
        rainfalls.append(rainfall)
        dates.append(current_date)
        t_max.append(high)
        t_min.append(low)

# Plot dates and rainfall(PRCP) values
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rainfalls, color="green")
ax.plot(dates, t_max, color="red", alpha=0.5)
ax.plot(dates, t_min, color="blue", alpha=0.5)
ax.fill_between(dates, t_max, t_min, facecolor="yellow", alpha=0.1)

# Format plot
ax.set_title("Rainfall Record - 2021", fontsize=20)
ax.set_xlabel("", fontsize=14)
ax.set_ylabel("Rainfall (PRCP)", fontsize=14)

plt.show()