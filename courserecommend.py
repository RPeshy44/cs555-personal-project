# The information used in this program is based primarily off of the Stevens Computer Science Wiki's Undergraduate page as of May 2023: https://www.srcit.stevens.edu/wiki/index.php?title=Undergraduate
# Course requirements were gathered from the course sections listed for Spring 2023 and Fall 2023
# It is possible that changes in the curriculum for undergraduate computer science students at Stevens will cause the information in this program to be incomplete or incorrect.

# This program, when run, receives input from the user (an undergraduate computer science student) to determine which elective courses they are eligible for.

import electives

def getInput():
    # Initializes variables: userInput holds the value of the user's input, and userList records each of the courses the user inputs
    userInput = ""
    userList = []

    # Prints instructions for the user
    print("")
    print("INSTRUCTIONS: ")
    print("Please enter the course code for each computer science (CS) and mathematics (MA) course you will have finished before next semester.")
    print("Enter each course using the same format (capital letters, no spaces) as the following example: 'CS101'")
    print("Press the enter/return key after entering each individual course.")
    print("Type 'DONE' in all caps and press the enter/return key after you have entered every course.")
    print("")

    # Continuously asks the user to provide the course code for a course that they have taken until they enter "DONE".
    while userInput != "DONE":
        try:
            userInput = input("Enter a course: ")
        except EOFError:
            break
        if userInput != "DONE":
            userList.append(userInput)

    # Prints the list of the user's entered courses.
    print("")
    print("YOUR COMPLETED COURSES: ")
    print(userList)
    print("")
    print("")

    return userList

def showElectives():
    # Initializes variables: electivesList contains all of the Elective objects for the possible elective courses
    electivesList = electives.allElectives()


    print("YOU ARE ELIGIBLE FOR THE FOLLOWING ELECTIVES: ")
    print("")

    # IN ITS CURRENT STATE, THIS PRINTS ALL THE POSSIBLE ELECTIVE COURSES, REGARDLESS OF THE USER'S INPUT.
    print("Software Development Electives: ")
    for elective in electivesList:
        if elective.sd:
            print(elective.id + " - " + elective.name)

    print("")

    print("Technical Electives: ")
    for elective in electivesList:
        if elective.tech:
            print(elective.id + " - " + elective.name)

    print("")
    print("Please note that any courses that appear in both categories (Software Development Electives and Technical Electives) can only be used as credit for one category or the other, not both.")
    print("")

    return electivesList

if __name__ == '__main__':
    # Calling the two functions
    getInput()
    showElectives()