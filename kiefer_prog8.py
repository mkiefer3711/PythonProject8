import csv
import os
# Function for opening and reading the file, and creating a dictionary using it
def file_to_dictionary(file_name):
    # Creates an empty dictionary
    mydict = {}
    try:
        # Opens and reads the csv file
        with open(file_name , mode = "r")as file:
            dictionary = csv.DictReader(file)
            # For loop that goes through each line for the dictionary
            for lines in dictionary:
                # Sets name equal to lines at the Trench name
                name = lines["ï»¿Trench Name"]
                # Sets depth equal to lines at the Max Depth
                depth = lines["  Max Depth (m)"]
                # Sets name to the key and depth as an int to the value for the dictionary
                mydict[name] = int(depth)
            # Returns the newly created dictionary
            return mydict
    except:
        print("File does not exsist")
# Function to sort the dictionary in alphabetical order by name    
def display_by_name(dict):
    print("Trench Data Sorted by Name\n")
    count = 0
    # Creates an empty list for the names
    name_list = []
    # Gets each name in the dictionary and adds them to the empty name_list
    for name in dict:
        name_list.append(name)
    # Sorts the name_list
    name_list.sort()
    print(f"{'#' : <5}{'Trench' : <35} {'Depth(m)' : <35}")
    print("-------------------------------------------------")
    #For loop that gets each depth for the sorted names and prints the names and depths
    for name in name_list:
        depth = dict[name]
        count = count + 1
        print(f"{count : <5}{name : <35} {depth : >6}")
# Function that sorts by largest depth to smallest depth     
def display_by_depth(dict):
    print("Trench Data Sorted by Depth\n")
    # Creates an empty list and empty dictionary
    depth_list = []
    depth_dict = {}
    count = 0
    # For loop that will make depth the new key in the dictionary
    for name in dict:
        depth = dict[name]
        depth_dict[depth] = name
    # For loop that adds all of the depths to a new list
    for depth in depth_dict:
        depth_list.append(depth)
    # Sorts the list and reverses it so largest depths come first
    depth_list.sort(reverse=True)
    print(f"{'#' : <5}{'Trench' : <35} {'Depth(m)' : <13}{'Depth(ft)' : <}")
    print("---------------------------------------------------------------")
    # For loop that gets the name for each depth and converts depth to feet
    for depth in depth_list:
        name = depth_dict[depth]
        feet = round(depth*3.28, 1)
        count = count + 1
        print(f"{count : <5}{name : <35}{depth : >6}{feet: >15}")
# Function to sort by the length of the names     
def display_by_length(dict):
    print("Trench Data Sorted by Name Length\n")
    # Creates an empty list and empty tuple
    length_list = []
    length_tuple = []
    count = 0
    # For loop that add the length of the name and the name to a tuple
    for name in dict:
        length_tuple.append([len(name), name])
    # Sort the tuple
    length_tuple.sort()
    print(f"{'#' : <5}{'Trench' : <35} {'Depth(m)' : <35}")
    print("------------------------------------------------")
    # For loop that gets each name at position 1 in the tuple and gets the depths for the dictionary
    for trench in length_tuple:
        name = trench[1]
        depth = dict[name]
        count = count + 1
        print(f"{count : <5}{name : <35}{depth : >6}")    
# Function that will ask user for inputs     
def menu():
    user_input = " "
    # While loop that loops if the user input doesn't equal Q
    while user_input != "Q":
        # Sets user_input equal to what they input
        user_input = input("NDLQ:")
        # Changes the user_input to uppercase
        user_input = user_input.upper()
        # If user_input is N,D,L, or Q it will return that letter
        if user_input == "N" or user_input == "D" or user_input == "L" or user_input == "Q":
            return user_input
        # Any other input it will say that it is not a valid command
        else:
            print(user_input, "is not a valid command")      
# Main function where the program starts   
def main():
    user_input = " "
    # Calls the file_to_dictionary function on the csv file
    dict = file_to_dictionary("Trench_Depths.csv")
    if dict != None:
        # While loop that displays options and will loop as long as input is not Q
        while user_input != "Q":
            print("\n\nTrench Report Control\n\nN = Display data by (N)ame\nD = Display data by (D)epth\nL = Display data by Name (L)ength\nQ = Quit (terminate)\n")
            # Calls the menu function to get the user_input
            user_input = menu()
            # Clears the output window before each repetition begins
            os.system('cls')
            # If statements that call different functions depending on the user_input
            if user_input == "N":
                display_by_name(dict)
            if user_input == "D":
                display_by_depth(dict)
            if user_input == "L":
                display_by_length(dict)
# Calls the main function
main()
