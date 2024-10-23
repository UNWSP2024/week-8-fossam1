#Samuel Foss
#Program 3 capital quiz
#10/23

# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys,
# and their capitals as values.
# The program should then randomly quiz the user by displaying the name of a state
# and asking the user to enter the state's capital.
# The program should count of the number of correct and incorrect responses.
# (You could alternatively use another country and provinces,
# or countries of the world and capitals).

import random

#US states and Capitals pulled in alphabetical order from a google list of states and capitals
statesandcapitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}




def main():
    correct = 0
    incorrect = 0

    allstates = list(statesandcapitals.keys())
    random.shuffle(allstates)

    for state in allstates:
        answer = input(f"The capital of {state} is: ").strip()

        if answer.lower() == statesandcapitals[state].lower():
            correct += 1

        else:
            incorrect += 1

    print(f"You correctly answered {correct} capitals correctly and {incorrect} capitals incorrectly!")

main()



#Output - I spammed letters to demonstrate the incorrect aspect of my code
#The capital of Wisconsin is: madison
#The capital of Massachusetts is: Salem
#The capital of Tennessee is: Nashville
#The capital of Rhode Island is: Providence
#The capital of Colorado is: Carson
#The capital of Virginia is: e
#The capital of New York is: e
#The capital of Wyoming is: e
#The capital of Mississippi is: e
#The capital of Oregon is: e
#The capital of Oklahoma is: e
#The capital of Kentucky is: e
#The capital of Minnesota is: e
#The capital of Idaho is: e
#The capital of New Mexico is: e
#The capital of Arkansas is: e
#The capital of Iowa is: e
#The capital of Louisiana is: e
#The capital of South Carolina is: e
#The capital of Kansas is: e
#The capital of Utah is: e
#The capital of Pennsylvania is: e
#The capital of Georgia is: e
#The capital of Nebraska is: e
#The capital of California is: e
#The capital of Texas is: d
#The capital of Connecticut is: d
#The capital of Ohio is: fa
#sThe capital of Maryland is: fa
#sThe capital of Montana is: f
#The capital of New Jersey is: s
#The capital of New Hampshire is: fas
#The capital of Illinois is:
#The capital of Missouri is: f
#The capital of Arizona is: w
#The capital of Michigan is: w
#The capital of Maine is: w
#The capital of North Carolina is: w
#The capital of Indiana is: Indianapolis
#The capital of Vermont is: Montpelier
#The capital of South Dakota is: Pierre
#The capital of North Dakota is: Bismarck
#The capital of West Virginia is: w
#The capital of Hawaii is: w
#The capital of Delaware is: w
#The capital of Florida is: w
#The capital of Washington is: w
#The capital of Alaska is: w
#The capital of Nevada is: w
#The capital of Alabama is: w
#You correctly answered 7 capitals correctly and 43 capitals incorrectly!

#Process finished with exit code 0
