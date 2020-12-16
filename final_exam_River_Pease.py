import re

# Function to find the mode
def most_frequent(nums):
    counter = 0
    num = nums[0]

    for number in nums :
        frequency = nums.count(number)
        if frequency > counter :
            counter = frequency
            num = number

    return num

# Open the file
data = open('ping.txt')

# Initial count of pings
count = 0

# Empty list of times
times = []

for line in data :
    line.rstrip()
    if not line.startswith("64 bytes from ") :
        continue
    # Count number of pings
    count += 1

    phrases = line.split()
    for phrase in phrases :
        if not phrase.startswith("time=") :
            continue
        times_lst = re.findall(r'-?\d+\.?\d*', phrase)
        # Convert list of lists to list of floats
        for time in times_lst :
            times.append(float(time))

# Find average
avg_time = sum(times) / len(times)


print("Ping ran", count, "times")
print("The average return time was", avg_time, "ms")
print("The mode was", most_frequent(times), "ms")
