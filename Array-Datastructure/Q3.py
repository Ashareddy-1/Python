#Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
odd_numbers = []
max_number = input('Enter your max number')
for i in range(1,int(max_number)+1):
    if i%2 != 0:
        odd_numbers.append(i)
print(odd_numbers)
        
