import numpy as np

# Temperature data for 7 days
temp = np.array([30, 32, 35, 31, 29, 28, 34])

print("Temperature Data (°C):", temp)

# Average temperature
avg_temp = np.mean(temp)
print("Average Temperature:", avg_temp)

# Maximum temperature
max_temp = np.max(temp)
print("Maximum Temperature:", max_temp)

# Minimum temperature
min_temp = np.min(temp)
print("Minimum Temperature:", min_temp)

# Days above average
above_avg = temp[temp > avg_temp]
print("Days with Temperature Above Average:", above_avg)
