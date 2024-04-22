class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, assignment, grade):
        self.grades[assignment] = grade

    def calculate_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def __str__(self):
        return f"Student: {self.name}, Grades: {self.grades}"


class GradeTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        self.students[name] = Student(name)

    def add_grade(self, student_name, assignment, grade):
        if student_name in self.students:
            self.students[student_name].add_grade(assignment, grade)
        else:
            print(f"Student {student_name} not found!")

    def calculate_average_grade(self, student_name):
        if student_name in self.students:
            return self.students[student_name].calculate_average_grade()
        else:
            print(f"Student {student_name} not found!")
            return 0

    def generate_grade_report(self):
        print("Grade Report")
        print("-------------")
        for name, student in self.students.items():
            print(f"{name}: {student.calculate_average_grade()}")

    def __str__(self):
        return "\n".join(str(student) for student in self.students.values())


# Example Usage
grade_tracker = GradeTracker()

# Add students
grade_tracker.add_student("Alice")
grade_tracker.add_student("Bob")

# Add grades
grade_tracker.add_grade("Alice", "Math", 90)
grade_tracker.add_grade("Alice", "Science", 85)
grade_tracker.add_grade("Bob", "Math", 88)
grade_tracker.add_grade("Bob", "Science", 92)

# Generate grade report
grade_tracker.generate_grade_report()
