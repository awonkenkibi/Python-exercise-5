# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits= ["banana", "apple", "strawberry", "pineapple", "blueberry"]
# TODO: Add a fruit to the end of the list
fruits.append("kiwi")
# TODO: Insert a fruit at the beginning of the list
fruits.insert(0,"pineapple")
# TODO: Remove a fruit from the list
fruits.remove("blueberry")
# TODO: Print the modified list
print(fruits)


#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
list=[1,2,3,4,5]
# TODO: Create a new list with each number squared
squared_list=[x**2 for x in list]
# TODO: Find the sum and average of the original numbers
total_sum= sum(list)
print(total_sum)
average= total_sum/len(list)
print(average)
# TODO: Print the results
print(list)
print(squared_list)

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
countries_capitals= {
    "South Africa": "Pretoria",
    "Zimbabwe":"Harare",
    "Japan": "Tokyo"

    
}
# TODO: Add a new country-capital pair
countries_capitals["Lesotho"] ="Maseru"

# TODO: Update the capital of an existing country
countries_capitals["South Africa"]= "Cape Town"
print(countries_capitals["South Africa"])
# TODO: Remove a country-capital pair
del countries_capitals["Japan"]
# TODO: Print the modified dictionary
print(countries_capitals)
#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruit_colors={'apple': 'green', 
              'pineapple': 'yellow', 
              'grape': 'purple'
}
# TODO: Print all the fruits (keys)
# for fruit in fruit_colors:
#     print(fruit)
print(fruit_colors.keys())
# TODO: Print all the colors (values)
print(fruit_colors.values())
# TODO: Print each fruit and its color

print(fruit_colors)

# TODO: Check if a fruit is in the dictionary and print its color
# 
key = fruit_colors.keys()
values = fruit_colors.get("apple")
print(values)
#