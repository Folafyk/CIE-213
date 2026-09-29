students = {}
conflicts = set()
graph = {}
colors = {}



def enter_students():
    global students

    students = {}

    print("\nStudent Course Registration")
    print("===========================")

    number_of_students = int(input("Enter number of students: "))

    for i in range(number_of_students):

        student_name = input(
            f"\nEnter name of Student {i + 1}: "
        )

        number_of_courses = int(
            input(f"Enter number of courses for {student_name}: ")
        )

        courses = []

        for j in range(number_of_courses):

            course = input(
                f"Enter course {j + 1}: "
            ).upper()

            courses.append(course)

        students[student_name] = courses

    print("\nStudent registrations saved successfully.")


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

    day, time = exam_periods[time_slot - 1]

    print(f"\n{day} - {time}")

    for course in timetable[time_slot]:

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

while True:

    print("\n")
    print("==============================")
    print(" COURSE REGISTRATION SYSTEM")
    print("==============================")

    print("1. Enter Student Registrations")
    print("2. View Course Conflicts")
    print("3. Generate Exam Timetable")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        enter_students()

    elif choice == "2":

        view_conflicts()

    elif choice == "3":

        generate_timetable()

    elif choice == "4":

        print("\nThank you for using the system.")
        break

    else:

        print("\nInvalid choice. Please try again.")