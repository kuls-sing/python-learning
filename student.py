class Student:
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades if grades is not None else []
    
    def add_grade(self, grades):
        self.grades.append(grades)
        print(f"Grade {grades} added.")
        
    def average(self):
        if len(self.grades) == 0:
            print("No grades yet.")
            return
        avg = sum(self.grades) / len(self.grades)
        print(f"Average: {avg:.2f}")
    
    def __str__(self):
        return f"Student: {self.name} | Grades: {self.grades}"
    
s1 = Student("Alice")
print(s1)
s1.add_grade(85)
s1.add_grade(90)
s1.add_grade(78)
print(s1)
s1.average()
