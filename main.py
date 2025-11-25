

from hello import Room, Student, Teacher

room = Room()
room.add_person(Student("Ali", 20, 80))
room.add_person(Student("Sara", 19, 45))
room.add_person(Student("John", 21, 60))
room.add_person(Teacher("Ms. Smith", 35, "Math"))
room.add_person(Teacher("Mr. Doe", 40, "English"))

print("Teachers in room:")
for teacher in room.get_teachers():
    print(f"{teacher.name} (Age: {teacher.age}, Subject: {teacher.subject})")

print("\nStudents in room:")
for student in room.get_students():
    print(f"{student.name} (Age: {student.age}, Grade: {student.grade})")

print("\nTotal students:", room.count_students())
print("Successful students:", room.count_successful_students())

room.delete_student("Sara")

print("\nAfter deleting Sara:")
print("Total students:", room.count_students())
print("Successful students:", room.count_successful_students())
for student in room.get_students():
    print(f"{student.name} (Age: {student.age}, Grade: {student.grade})")
