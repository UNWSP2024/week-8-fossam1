#Samuel Foss
#Program 5 Course Info
#10/23

# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."
# Then ask the user for a subject (like "COS").
# Finally, the program will display the ID and name of all the courses having that subject.

courses = {
    "COS 2005": "Python Programming",
    "COM 2008": "Film Appreciation",
    "Mat 1005": "Math For The Liberal Arts",
    "PHE 1066": "Fitness and Health for Life",
    "SCI 1015": "Environmental Sci & Sustnablty"
}

subject = input("Input a subject for filtering: ").upper()

for coursecode, name in courses.items():
    if coursecode.startswith(subject):
        print(f"{coursecode} {name}")

#Output
#Input a subject for filtering: CoM
#COM 2008 Film Appreciation

#Process finished with exit code 0
