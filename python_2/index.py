import random

# Constants
EGGS = 1
FOOD_FEED = 2
CHICKEN = 3
TURKEY = 4

# Create the categories list
poultryCategories = ["Eggs", "Food/Feed", "Chicken", "Turkey"]

# Variables
userContinue = True

# File names
file_names = {
    EGGS: "eggs.txt",
    FOOD_FEED: "food_feed.txt",
    CHICKEN: "chicken.txt",
    TURKEY: "turkey.txt"
}

# Function to read tips from a file
def read_tips(filename):
    try:
        with open(filename, 'r') as file:
            tips = file.read().splitlines()
        return tips
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []

# Function to write a new tip to a file
def write_tip(filename, tip):
    with open(filename, 'a') as file:
        file.write(tip + '\n')

# Load tips from files
eggsTips = read_tips(file_names[EGGS])
foodorfeedTips = read_tips(file_names[FOOD_FEED])
chickenTips = read_tips(file_names[CHICKEN])
turkeyTips = read_tips(file_names[TURKEY])

# Function to display the intro message
def intro():
    print("Hello! This program will give you free, useful, and personalized tips to help you take care of your birds!")
    print("These are the categories you may choose. Please type the number of the selected choice:")

# Function to display categories
def display_categories():
    number = 1
    for category in poultryCategories:
        print(number, category)
        number += 1

# Function to get a random tip
def get_random_tip(tips):
    if tips:
        return tips[random.randint(0, len(tips) - 1)]
    else:
        return "No tips available for this category."

# Function to handle user's choice and provide a tip
def provide_tip(userChoice):
    if userChoice == EGGS:
        print(get_random_tip(eggsTips))
    elif userChoice == FOOD_FEED:
        print(get_random_tip(foodorfeedTips))
    elif userChoice == CHICKEN:
        print(get_random_tip(chickenTips))
    elif userChoice == TURKEY:
        print(get_random_tip(turkeyTips))
    else:
        print("Invalid choice. Please select a valid category.")

# Function to add a new tip
def add_tip(userChoice):
    new_tip = input("Enter the new tip: ").strip()
    if userChoice == EGGS:
        eggsTips.append(new_tip)
        write_tip(file_names[EGGS], new_tip)
    elif userChoice == FOOD_FEED:
        foodorfeedTips.append(new_tip)
        write_tip(file_names[FOOD_FEED], new_tip)
    elif userChoice == CHICKEN:
        chickenTips.append(new_tip)
        write_tip(file_names[CHICKEN], new_tip)
    elif userChoice == TURKEY:
        turkeyTips.append(new_tip)
        write_tip(file_names[TURKEY], new_tip)
    else:
        print("Invalid choice. Please select a valid category.")

# Main program logic
intro()
display_categories()

while userContinue:
    try:
        userChoice = int(input("Please select a choice that is listed above, Type the number of the choice you desire for an easier user experience: "))
        provide_tip(userChoice)
        
        userAnswer = input("Would you like to add a new tip? Type (Y) for Yes, or (N) for No, for an easier user experience Y/N: ").strip().upper()
        if userAnswer == "Y":
            add_tip(userChoice)
        
        userAnswer = input("Another tip? Type (Y) for Yes, or (N) for No, for an easier user experience Y/N: ").strip().upper()
        if userAnswer != "Y":
            userContinue = False
    except ValueError:
        print("Invalid input. Please enter a number corresponding to your choice.")

# Thank you message
print("Thank you so much for using the program! Can't wait to see you next time!")
