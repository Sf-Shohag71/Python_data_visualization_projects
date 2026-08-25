import plotly.express as px
from die import Die

# Create two D6 dice game
die_1 = Die()
die_2 = Die()

results = []
for _ in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results
frequiencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequiencies.append(frequency)

# Visualize the results
title = "Rolling two D6 dies 1000 times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x = poss_results, y = frequiencies, title=title, labels=labels)

# Update layout
fig.update_layout(xaxis_dtick=1)

fig.show()