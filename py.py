COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

# def covers(sot):
#     final_list = []
#     for course in COURSES.keys():
#         if len((COURSES[course].intersection(sot))) > 0:
#             final_list.append(course)
#     print(final_list)
#     return final_list


def covers_all(sot):
    final_list = []
    for course in COURSES.keys():
        if COURSES[course].intersection(sot) == sot:
            final_list.append(course)
    print(final_list)
    return final_list

covers_all({"conditions", "input"})
