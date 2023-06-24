
print("Hello, this is your personal package loader. Read and follow the steps below:\n ")

#Ask user for the number of item
while True:
    try:
        number_of_items = int(input("Please enter the number of items you want to ship:\n "))
    except ValueError:
        print("Not a valid number. Try again. ")
        continue
    else:
        break

package_weight = 0

package_sent = 0

package_total_weight = 0

max_unused_capacity = 0 

package_with_most_empty_space = 0

count_packages = 0

new_unused_capacity = 0


#Ask user for the weight of each item
for item in range (number_of_items):

    item_weight = int(input("Please provide the weight of the item: "))


#If the weight is not between 1 and 10 kg, print an error message and stop the program
    if item_weight > 10 or item_weight < 1:
            print("Item weight not supported")
            break
    #Check if the weight is between 1 and 10 kg
    if item_weight >=1 or item_weight <= 10:
        package_weight = package_weight + item_weight

#If the weight is between 1 and 10 kg, add it to the package
#If the weight is between 1 and 10 kg and the package is not full, add the weight to the package
#If the weight is between 1 and 10 kg and the package is not full and it is the last item, send the package
    if package_weight == 20:
        package_sent = package_sent + 1
        package_total_weight = package_total_weight + package_weight
        new_unused_capacity = 0

              #this helps to understand how much weight and number of packages anytime the user adds
        print(f"Weight: {package_weight}. Number of packages: {package_sent + 1}")
        

#If the weight is between 1 and 10 kg and the package is full, send the item and start a new one 
    elif package_weight > 20:
        count_packages = count_packages + 1
        package_total_weight = package_total_weight + package_weight - item_weight
        package_sent = package_sent + 1
        #Print the leftover weight
        print("Package exceeds 20 kg. We will prepare another package. First package sent, weight amount: \n" + str(package_total_weight))
        print(f"Leftover weight:  {item_weight}")
        new_unused_capacity = 20 - package_weight
        package_weight = item_weight

    elif item == number_of_items - 1:
        package_sent = package_sent + 1
        package_total_weight = package_total_weight + package_weight
        new_unused_capacity = 20 - package_weight

    if new_unused_capacity > max_unused_capacity:
        max_unused_capacity = new_unused_capacity
        package_with_most_empty_space = package_sent


#Print the number of sent packages
#Print the weight of sent packages
#Print the package with the most empty space

print(package_weight)
if package_weight >0:
    count_packages += 1
print(f"Sent packages:  + {count_packages} ")
print(f"Sent weight: {package_total_weight}")
print(f"Package with most empty space:  {package_with_most_empty_space}")



