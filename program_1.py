#Samuel Foss
#program 1 initials
#10/23/24

# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names,
# and displays their first, middle, and last initials.
# For example, if the user enters John William Smith, the program should display J. W. S.

# Add your logic starting on line 11

def initials_generator(personsName):
    names = personsName.split()
    personsInitials = ""
    #    Add your logic here
    for part in names:
        personsInitials += part[0].upper() + ". "

    return personsInitials.strip()

personsName = input('Enter the users first, middle, and last name: ')

initials = initials_generator(personsName)

print(initials)

#Output
#Enter the users first, middle, and last name: John Denver Adam
#J. D. A.

#Process finished with exit code 0
