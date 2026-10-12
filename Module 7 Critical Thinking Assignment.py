course_rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}
course_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}
course_times = {
    "CSC101": "9:00am",
    "CSC102": "10:00am",
    "CSC103": "11:00am",
    "NET110": "12:00pm",
    "COM241": "1:00pm"
}
course_number = input("Enter the course number: " )
if course_number in course_rooms:
    print("Room Number:", course_rooms[course_number])
    print("Course Instructor:", course_instructors[course_number])
    print("Course Time:", course_times[course_number])
else:
    print("Sorry, your result cannot be found.")
