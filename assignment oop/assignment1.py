# ------------------- University Management System -------------------

# 1. Base Class: Person
class Person:
    total_people = 0  

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.total_people += 1  
    def introduce(self):
        print(f"Hi, I am {self.name}, {self.age} years old.")

    # 5. Class method to get total people
    @classmethod
    def get_total_people(cls):
        print(f"Total people created: {cls.total_people}")

# 2. Derived Class: Student
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.course_list = []
        self.__gpa = 0.0  

    def enroll_course(self, course):
        self.course_list.append(course)
        print(f"{self.name} has enrolled in {course}.")

    def show_courses(self):
        if self.course_list:
            print(f"{self.name} is enrolled in:")
            for c in self.course_list:
                print(f"- {c}")
        else:
            print(f"{self.name} has not enrolled in any courses.")

    # 4. Encapsulation: GPA getter & setter
    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        if 0.0 <= value <= 4.0:
            self.__gpa = value
            print(f"{self.name}'s GPA is set to {self.__gpa}")
        else:
            print("Invalid GPA! Must be between 0.0 and 4.0.")

    # 6. Static Method
    @staticmethod
    def is_valid_id(student_id):
        if student_id.startswith("S-"):
            print(f"{student_id} is a valid Student ID.")
        else:
            print(f"{student_id} is NOT a valid Student ID.")

# 2. Derived Class: Teacher
class Teacher(Person):
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject

    # Override introduce
    def introduce(self):
        print(f"I am Professor {self.name}, teaching {self.subject}.")

# 3. Polymorphism function
def display_role(person):
    if isinstance(person, GraduateStudent):
        print(f"{person.name} is a Graduate Student with thesis '{person.thesis_title}'.")
    elif isinstance(person, Student):
        print(f"{person.name} is a Student with ID {person.student_id}.")
    elif isinstance(person, Teacher):
        print(f"{person.name} is a Teacher of {person.subject}.")
    else:
        print(f"{person.name} is a Person.")

# 7. GraduateStudent (Multilevel Inheritance)
class GraduateStudent(Student):
    def __init__(self, name, age, student_id, thesis_title):
        super().__init__(name, age, student_id)
        self.thesis_title = thesis_title

    # Override introduce
    def introduce(self):
        print(f"Hi, I am {self.name}, a Graduate Student working on '{self.thesis_title}'.")

# ------------------- Testing -------------------

# Create objects
p1 = Person("Alice", 40)
s1 = Student("Moon", 21, "S-123")
g1 = GraduateStudent("Ali", 25, "S-543", "AI in Robotics")
t1 = Teacher("Dr. Rizvi", 40, "T-678", "Mathematics")

# Introduce
p1.introduce()
s1.introduce()
g1.introduce()
t1.introduce()

# Student actions
s1.enroll_course("Math 101")
s1.enroll_course("Physics 101")
s1.show_courses()

# GPA
s1.gpa = 3.8
print(f"GPA of {s1.name}: {s1.gpa}")

# Static method
Student.is_valid_id(s1.student_id)
Student.is_valid_id("12345")

# Polymorphism
display_role(s1)
display_role(g1)
display_role(t1)
display_role(p1)

# Total people
Person.get_total_people()
