import pandas as pd

df = pd.read_csv('demo-audio-data.csv', header=None)
cutoff = 15040

# Assuming the first row is also data, not header
# If it was a header, we would use df = pd.read_csv('demo-audio-data.csv')

filtered_numbers = df[df[0] > cutoff]
answer = filtered_numbers[0].sum()

print(int(answer))
