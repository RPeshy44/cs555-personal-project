# The information used in this program is based primarily off of the Stevens Computer Science Wiki's Undergraduate page as of May 2023: https://www.srcit.stevens.edu/wiki/index.php?title=Undergraduate
# Course requirements were gathered from the course sections listed for Spring 2023 and Fall 2023
# It is possible that changes in the curriculum for undergraduate computer science students at Stevens will cause the information in this program to be incomplete or incorrect.


# id is a string that holds the course code (Example: "CS101")
# name is a string that holds the full name of the course (Example: "Intro to Programming")
# sd is a bool that states whether or not the course is considered to satisfy a "Software Development Elective" requirement
# tech is a bool that states whether or not the course is considered to satisfy a "Technical Elective" requirement
# requirement is a list that contains strings that hold the course codes of all courses required to be considered eligible for this course (Example: ["CS101", "CS111"])
class Elective:
    def __init__(self, id, name, sd, tech, requirement):
        self.id = id
        self.name = name
        self.sd = sd
        self.tech = tech
        self.requirement = requirement


# Any course that is commented out below was found to be offered in neither Spring 2023 nor Fall 2023 despite appearing on the wiki.

cs503 = Elective("CS503", "Discrete Math for Cryptography", False, True, ["CS135"])
cs513 = Elective("CS513", "Knowledge Dis & Data Mining", False, True, [])
cs516 = Elective("CS516", "Compiler Design", True, True, ["CS334","CS385"])
cs521 = Elective("CS521", "TCP/IP Networking", True, True, ["CS492"])
cs522 = Elective("CS522", "Mobile Systems and Applications", True, True, ["CS385"])
# cs523 = Elective("CS523", "Programming the Internet of Things using iOS", True, True, [""])
cs524 = Elective("CS524", "Intro to Cloud Computing", False, True, ["CS492"])
cs526 = Elective("CS526", "Enterprise & Cloud Computing", True, True, ["CS385"])
# cs537 = Elective("CS537", "Interactive Computer Graphics", True, False, [""])
cs541 = Elective("CS541", "Artificial Intelligence", True, True, ["MA222","MA232"])
cs545 = Elective("CS545", "Human-Computer Interaction", False, True, ["CS385"])
cs546 = Elective("CS546", "Web Programming", True, True, ["CS146","CS442"])
cs548 = Elective("CS548", "Enterprise Software Archi & Dgn", True, True, ["CS385"])
cs549 = Elective("CS549", "Distrib Sys & Cloud Computing", True, True, ["CS385"])
# cs553 = Elective("CS553", "Intro Text Mining/Nat. Lang Proc", False, True, [""])
cs554 = Elective("CS554", "Web Programming II", True, True, ["CS546"])
cs555 = Elective("CS555", "Agile Methods for Software Development", True, False, [])
# cs557 = Elective("CS557", "Intro to Natural Language Proc", False, True, [""])
cs558 = Elective("CS558", "Computer Vision", True, True, ["CS385","MA232"])
cs559 = Elective("CS559", "Machine Learning: Fund & Apps", False, True, ["MA222","MA232"])
cs562 = Elective("CS562", "Database Management Systems II", False, True, ["CS442"])
cs573 = Elective("CS573", "Fundamentals of CyberSecurity", False, True, ["CS385"])
cs574 = Elective("CS574", "Object-Oriented Anal. & Dsng.", False, True, ["CS385"])
cs576 = Elective("CS576", "Systems Security", False, True, ["CS306","CS392"])
# cs577 = Elective("CS577", "Reverse Engineering and Application Analysis", False, True, [""])
cs578 = Elective("CS578", "Privacy in a Networked World", False, True, ["CS306"])
# cs581 = Elective("CS581", "Online Social Networks", False, True, [""])
# cs582 = Elective("CS582", "Causal Inference", False, True, [""])
cs583 = Elective("CS583", "Deep Learning", False, True, ["MA232"])
cs584 = Elective("CS584", "Natural Language Processing", False, True, [])
cs600 = Elective("CS600", "Adv. Algorithm Dsgn & Implement", False, True, ["CS385"])
cs615 = Elective("CS615", "Systems Administration", False, True, ["CS492"])
# cs643 = Elective("CS643", "Formal Verif of Software", False, True, [""])
# cpe358 = Elective("CPE358", "Switching Theory and Logical Design", False, True, [""])


# Initializes variables: userInput holds the value of the user's input, userList records each of the courses the user inputs, and electivesList contains all of the Elective objects for the possible elective courses.
userInput = ""
userList = []
electivesList = [cs503, cs513, cs516, cs521, cs522, cs524, cs526, cs541, cs545, cs546, cs548, cs549, cs554, cs555, cs558, cs559, cs562, cs573, cs574, cs576, cs578, cs583, cs584, cs600, cs615]