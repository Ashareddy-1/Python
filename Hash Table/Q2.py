#nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
#What was the temperature on Jan 9?
#What was the temperature on Jan 4?
#Figure out data structure that is best for this problem

#1
temperatures = {}

with open(r'C:\\Users\\SESA610197\\Documents\\AIMLLNG\\Python Learning\\Hash Table\\nyc_weather.csv', "r") as f:
    next(f)  # Skip the header row if there is one
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        temp = float(tokens[1])  # Convert temperature to float
        temperatures[day] = temp

print(temperatures)
print(temperatures['Jan 9'])
print(temperatures['Jan 4'])
