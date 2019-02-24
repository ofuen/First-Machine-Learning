import numpy as np

x = np.random.randint(low=0, high=100, size=100)

# Compute frequency and bins
frequency, bins = np.histogram(x, bins=10, range=[0, 100])

# Pretty Print
for b, f in zip(bins[1:], frequency):
    print(round(b, 1), ''.join(np.repeat('*', f)))
