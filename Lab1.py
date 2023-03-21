students = []
courses = []

def getstudent():
    n = int(input("Enter the number of students:"))
    for i in range(n):
        student = {
            'name': '',
            'id': '',
            'dob': '',
        }
        print(f"Information of student number {i+1}:")
        name = input("Enter name of student:")
        id = int(input("Enter id of student:"))
        dob = input("Enter date of birth:")
        student['id'] = id
        student['name'] = name
        student['dob'] = dob
        students.append(student)

def showstudents():
    i = 0
    for student in students:
        i = i+1
        print(f"Student{i}: name {student['name']}, id {student['id']}, dob {student['dob']}")

def getcourse():
    n = int(input("Enter the number of courses:"))
    for i in range(n):
        course = {
            "name": '',
            "id": '',
            "marks": {}
        }
        name = input("Enter name of course:")
        id = int(input("Enter id of course:"))
        course['name'] = name
        course['id'] = id
        courses.append(course)

def showcourses():
    i = 0
    for course in courses:
        i = i+1
        print(f"Course {i}: name {course['name']}, id {course['id']}")

def getmark():
    course_id = int(input("Enter id of course:"))
    course = None
    for c in courses:
        if c['id'] == course_id:
            course = c
            break
    if not course:
        print("This course could not be found")
        return
    for student in students:
        mark = float(input(f"Enter mark of student {student['name']}: "))
        course['marks'][student['id']] = mark

def showmarks():
    course_id = int(input("Enter id of course:"))
    course = None
    for c in courses:
        if c['id'] == course_id:
            course = c
            break
    if not course:
        print("This course could not be found")
        return
    print(f"List of marks for the course {course['name']}:")
    for student in students:
        if student['id'] in course['marks']:
            mark = course['marks'][student['id']]
            print(f"{student['name']}: {mark}")

while True:
    print("\nStudent management system\n")
    print("1. Input list of students")
    print("2. Input list of courses")
    print("3. Input mark for a course")
    print("4. List students")
    print("5. List courses")
    print("6. Student marks")
    print("0. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 0:
        break
    elif choice == 1:
        getstudent()
    elif choice == 2:
        getcourse()
    elif choice == 3:
        getmark()
    elif choice == 4:
        showstudents()
    elif choice == 5:
        showcourses()
    elif choice == 6:
        showmarks()
