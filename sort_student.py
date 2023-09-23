class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __repr__(self):
        return f"Student(name='{self.name}', roll_number='{self.roll_number}', cgpa={self.cgpa})"

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students
students = [
    Student("Alice", "A101", 3.7),
    Student("Bob", "B102", 3.9),
    Student("Charlie", "C103", 3.5),
    Student("David", "D104", 3.8),
]

sorted_students = sort_students(students)

for student in sorted_students:
    print(student)
