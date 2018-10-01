# 1.1
# Opens the file to (r)ead
f = open("temperatur.txt", "r")

# Initiates an empty list to store temperatures
avg_temp = []

# Runs through every line and adds the contents (already prepared integers)
for month in f:
    avg_temp.append(int(month))

# Closes file
f.close()

# 1.2
# A function that averages the contents of an argument list
def list_average(some_list):
    # Initiates a sum
    total = 0
    
    # Adds the contents of the list
    for i in range(len(some_list)):
        total += some_list[i]
    
    # Returns the sum of the elements divided by the number of elements    
    return float(total/len(some_list))

# Prints the results of the function with the readings from the file
print(list_average(avg_temp))
