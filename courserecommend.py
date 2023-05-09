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
    print("Please note that any input that is irrelevant or formatted incorrectly will not be recognized and will therefore not affect the list of courses for which you are eligible.")
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

    # Removes all duplicate entries and prints the list of the user's entered courses.
    userList = [*set(userList)]
    print("")
    print("YOU ENTERED THE FOLLOWING AS YOUR COMPLETED COURSES: ")
    print(userList)
    print("")
    print("")

    return userList

def showElectives(userList):
    # Initializes variables: electivesList contains all of the Elective objects for the possible elective courses, eligibleElectives will contain the Elective objects of the classes for which the user is eligible
    allElectives = electives.allElectives()
    eligibleElectives = []

    # Fills the list eleigibleELectives with the courses for which the user is eligible. 
    for electiveCourse in allElectives:
        if electiveCourse.requirement == []:
            eligibleElectives.append(electiveCourse)
        else:
            requirementsSatisfied = 0
            for requiredCourse in electiveCourse.requirement:
                for completedCourse in userList:
                    if completedCourse == requiredCourse:
                        requirementsSatisfied += 1
                if requirementsSatisfied == len(electiveCourse.requirement):
                    eligibleElectives.append(electiveCourse)


    print("YOU ARE ELIGIBLE FOR THE FOLLOWING ELECTIVES: ")
    print("")

    # Prints all courses for which the user is eligible that fall under the category of "Software Development Electives"
    print("Software Development Electives: ")
    for elective in eligibleElectives:
        if elective.sd:
            print(elective.id + " - " + elective.name)

    print("")

    # Prints all courses for which the user is eligible that fall under the category of "Technical Electives"
    print("Technical Electives: ")
    for elective in eligibleElectives:
        if elective.tech:
             print(elective.id + " - " + elective.name)

    print("")
    print("Please note that any courses that appear in both categories (Software Development Electives and Technical Electives) can only be used as credit for one category or the other, not both.")
    print("")

    return eligibleElectives

if __name__ == '__main__':
    # Main function
    showElectives(getInput())