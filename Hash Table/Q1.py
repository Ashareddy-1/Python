#nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
#What was the average temperature in first week of Jan
#What was the maximum temperature in first 10 days of Jan
#Figure out data structure that is best for this problem

#1
temperatures = []

with open(r'C:\\Users\\SESA610197\\Documents\\AIMLLNG\\Python Learning\\Hash Table\\nyc_weather.csv', "r") as f:
    next(f)  # Skip the header row if there is one
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        temp = float(tokens[1])  # Convert temperature to float
        temperatures.append(temp)

# Calculate the average temperature for the first week (first 7 days)
average_temp = sum(temperatures[0:7]) / len(temperatures[0:7])
print(f"The average temperature in the first week of January is {average_temp:.2f} degrees.")

#2
print(max(temperatures))
        
    
