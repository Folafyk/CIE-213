students = {}
conflicts = set()
graph = {}
colors = {}

def enter_students():

    global students

    students = {}

    print("\nStudent Course Registration")
    print("===========================")

    while True:

        try:

            number_of_students = int(
                input("Enter number of students: ")
            )

            if number_of_students > 0:
                break

            print("Please enter a number greater than 0.")

        except ValueError:

            print("Please enter a valid number.")

    for i in range(number_of_students):

        while True:

            student_name = input(
                f"\nEnter name of Student {i + 1}: "
            ).strip()

            if student_name == "":
                print("Student name cannot be empty.")

            elif student_name in students:
                print("This student already exists.")

            else:
                break

        while True:

            try:

                number_of_courses = int(
                    input(
                        f"Enter number of courses for {student_name}: "
                    )
                )

                if number_of_courses > 0:
                    break

                print("Please enter a number greater than 0.")

            except ValueError:

                print("Please enter a valid number.")

        courses = []

        for j in range(number_of_courses):

            while True:

                course = input(
                    f"Enter course {j + 1}: "
                ).strip().upper()

                if course == "":
                    print("Course name cannot be empty.")

                elif course in courses:

                    print(
                        "This course has already been entered."
                    )

                else:

                    courses.append(course)
                    break

        students[student_name] = courses

    print("\nStudent registrations saved successfully.")

def view_students():

    if not students:

        print("\nNo student registrations available.")
        print("Please enter student registrations first.")
        return

    print("\nStudent Registrations")
    print("=====================")

    for student, courses in students.items():

        print("\nStudent:", student)

        for course in courses:

            print("  -", course)

def create_conflicts():

    global conflicts

    conflicts = set()

    for courses in students.values():

        for i in range(len(courses)):

            for j in range(i + 1, len(courses)):

                conflict = tuple(
                    sorted([courses[i], courses[j]])
                )

                conflicts.add(conflict)

def view_conflicts():

    if not students:

        print("\nNo student data available.")
        print("Please enter student registrations first.")
        return

    create_conflicts()

    print("\nCourse Conflicts")
    print("================")

    if not conflicts:

        print("No course conflicts found.")
        return

    for course1, course2 in sorted(conflicts):

        print(course1, "<->", course2)

def view_conflict_details():

    if not students:

        print("\nNo student data available.")
        print("Please enter student registrations first.")
        return

    create_conflicts()

    print("\nCourse Conflict Details")
    print("=======================")

    if not conflicts:

        print("No course conflicts found.")
        return

    for course1, course2 in sorted(conflicts):

        print(f"\n{course1} <-> {course2}")

        students_in_conflict = []

        for student, courses in students.items():

            if course1 in courses and course2 in courses:

                students_in_conflict.append(student)

        print("Students causing this conflict:")

        for student in students_in_conflict:

            print("  -", student)

def create_graph():

    global graph

    graph = {}

    for courses in students.values():

        for course in courses:

            if course not in graph:

                graph[course] = []

    for course1, course2 in conflicts:

        graph[course1].append(course2)
        graph[course2].append(course1)

def view_graph():

    if not students:

        print("\nNo student data available.")
        print("Please enter student registrations first.")
        return

    create_conflicts()
    create_graph()

    print("\nCourse Conflict Graph")
    print("=====================")

    for course in sorted(graph):

        if graph[course]:

            print(
                course,
                "->",
                ", ".join(sorted(graph[course]))
            )

        else:

            print(
                course,
                "-> No conflicts"
            )

def color_graph():

    global colors

    colors = {}

    courses = sorted(
        graph,
        key=lambda course: len(graph[course]),
        reverse=True
    )

    for course in courses:

        used_colors = set()

        for neighbor in graph[course]:

            if neighbor in colors:

                used_colors.add(colors[neighbor])

        color = 0

        while color in used_colors:

            color += 1

        colors[course] = color

def generate_timetable():

    if not students:

        print("\nNo student data available.")
        print("Please enter student registrations first.")
        return

    create_conflicts()

    create_graph()

    color_graph()

    timetable = {}

    for course, color in colors.items():

        time_slot = color + 1

        if time_slot not in timetable:

            timetable[time_slot] = []

        timetable[time_slot].append(course)

    exam_periods = [

        ("Monday", "9:00 AM"),
        ("Monday", "1:00 PM"),

        ("Tuesday", "9:00 AM"),
        ("Tuesday", "1:00 PM"),

        ("Wednesday", "9:00 AM"),
        ("Wednesday", "1:00 PM"),

        ("Thursday", "9:00 AM"),
        ("Thursday", "1:00 PM"),

        ("Friday", "9:00 AM"),
        ("Friday", "1:00 PM")

    ]

    print("\nFinal Exam Timetable")
    print("====================")

    for time_slot in sorted(timetable):

        if time_slot <= len(exam_periods):

            day, time = exam_periods[time_slot - 1]

            print(f"\n{day} - {time}")

            for course in sorted(timetable[time_slot]):

                print("  -", course)

        else:

            print(f"\nTime Slot {time_slot}")

            for course in sorted(timetable[time_slot]):

                print("  -", course)

    print("\nChecking Timetable")
    print("==================")

    conflict_found = False

    for course1, course2 in conflicts:

        if colors[course1] == colors[course2]:

            print(
                "CONFLICT:",
                course1,
                "and",
                course2,
                "are scheduled at the same time."
            )

            conflict_found = True

    if not conflict_found:

        print("No scheduling conflicts detected.")

def search_student():

    if not students:

        print("\nNo student registrations available.")
        return

    name = input(
        "\nEnter student name to search: "
    ).strip()

    found = False

    for student, courses in students.items():

        if student.lower() == name.lower():

            print("\nStudent Found")
            print("=============")

            print("Name:", student)
            print("Courses:")

            for course in courses:

                print("  -", course)

            found = True
            break

    if not found:

        print("\nStudent not found.")

def search_course():

    if not students:

        print("\nNo student registrations available.")
        return

    course_name = input(
        "\nEnter course to search: "
    ).strip().upper()

    students_found = []

    for student, courses in students.items():

        if course_name in courses:

            students_found.append(student)

    print("\nCourse Search")
    print("=============")

    if not students_found:

        print("Course not found.")

    else:

        print("Course:", course_name)
        print("Registered students:")

        for student in students_found:

            print("  -", student)

def remove_student():

    if not students:

        print("\nNo student registrations available.")
        return

    name = input(
        "\nEnter student name to remove: "
    ).strip()

    student_to_remove = None

    for student in students:

        if student.lower() == name.lower():

            student_to_remove = student
            break

    if student_to_remove is None:

        print("\nStudent not found.")
        return

    confirmation = input(
        f"Are you sure you want to remove {student_to_remove}? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":

        del students[student_to_remove]

        print(
            f"\n{student_to_remove} has been removed successfully."
        )

    else:

        print("\nStudent removal cancelled.")

def remove_course():

    if not students:

        print("\nNo student registrations available.")
        return

    student_name = input(
        "\nEnter student name: "
    ).strip()

    actual_student = None

    for student in students:

        if student.lower() == student_name.lower():

            actual_student = student
            break

    if actual_student is None:

        print("\nStudent not found.")
        return

    course = input(
        "Enter course to remove: "
    ).strip().upper()

    if course not in students[actual_student]:

        print("\nThis student is not registered for that course.")
        return

    students[actual_student].remove(course)

    print(
        f"\n{course} has been removed from "
        f"{actual_student}'s registration."
    )

while True:

    print("\n")
    print("==========================================")
    print(" STUDENT COURSE REGISTRATION SYSTEM")
    print("==========================================")

    print("1. Enter Student Registrations")
    print("2. View Student Registrations")
    print("3. View Course Conflicts")
    print("4. View Conflict Details")
    print("5. View Conflict Graph")
    print("6. Generate Exam Timetable")
    print("7. Search Student")
    print("8. Search Course")
    print("9. Remove Student")
    print("10. Remove Course")
    print("11. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":

        enter_students()

    elif choice == "2":

        view_students()

    elif choice == "3":

        view_conflicts()

    elif choice == "4":

        view_conflict_details()

    elif choice == "5":

        view_graph()

    elif choice == "6":

        generate_timetable()

    elif choice == "7":

        search_student()

    elif choice == "8":

        search_course()

    elif choice == "9":

        remove_student()

    elif choice == "10":

        remove_course()

    elif choice == "11":

        print("\nThank you for using the system.")
        break

    else:

        print(
            "\nInvalid choice. "
            "Please enter a number from 1 to 11."
        )