from courserecommend import showElectives
import electives

# The getInput() function ensures that the list passed into showElectives as an argument contains no duplicate entries.

# User types "DONE" without inputting any courses; output should contain the three courses that have no requirement.
def test_showElectives1():
    assert showElectives([]) == [electives.cs513, electives.cs555, electives.cs584]

# User has entered "CS135"; output should contain the three courses that have no requirement plus the one course that requires CS135.
def test_showElectives2():
    assert showElectives(["CS135"]) == [electives.cs503, electives.cs513, electives.cs555, electives.cs584]

# User has entered the improperly formatted "CS 135"; output should contain only the three courses that have no requirement (since the input was improperly formatted according to the directions).
def test_showElectives3():
    assert showElectives(["CS 135"]) == [electives.cs513, electives.cs555, electives.cs584]

# User has entered "CS135" along with other irrelevant strings; output should contain the three courses that have no requirement plus the one course that requires CS135 (the irrelevant strings do not affect the output).
def test_showElectives4():
    assert showElectives(["Useless", "CS135", "Information"]) == [electives.cs503, electives.cs513, electives.cs555, electives.cs584]

# User has entered "CS135" along with other irrelevant info (a float and a bool); output should contain the three courses that have no requirement plus the one course that requires CS135 (the irrelevant entries do not affect the output).
def test_showElectives5():
    assert showElectives([1.21, "CS135", True]) == [electives.cs503, electives.cs513, electives.cs555, electives.cs584]

# User has entered "MA232" and "MA222" along with other irrelevant info of different types; output should contain the three courses that have no requirement, plus the one course that requires only MA232, plus the two courses that require both MA22 and MA232.
def test_showElectives6():
    assert showElectives(["MA232", -7, False, "MA222", 3.0049]) == [electives.cs513, electives.cs541, electives.cs555, electives.cs559, electives.cs583, electives.cs584]
    
# User has entered every possible required course, as well as extra courses, in no particular order; output should contain all known elective courses (25 total).
def test_showElectives7():
    assert showElectives(["MA222", "CS492", "CS115", "CS442", "CS334", "CS546", "CS392", "CS555", "CS146", "MA232", "CS306", "CS385", "CS135"]) == [electives.cs503, electives.cs513, electives.cs516, electives.cs521, electives.cs522, electives.cs524, electives.cs526, electives.cs541, electives.cs545, electives.cs546, electives.cs548, electives.cs549, electives.cs554, electives.cs555, electives.cs558, electives.cs559, electives.cs562, electives.cs573, electives.cs574, electives.cs576, electives.cs578, electives.cs583, electives.cs584, electives.cs600, electives.cs615]