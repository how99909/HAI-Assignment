class Student:
    student_id = 0
    name = ""
    age = 0
    
    def display_info(self):
        print(f"ID: {self.student_id}번 / 이름: {self.name} / 나이: {self.age}살")

class StudentManager:
    students = []
    
    def add_student(self, student):
        a = Student()
        a.student_id = student[0]
        a.name = student[1]
        a.age = student[2]
        self.students.append(a)
        
    def display_all_students(self):
        for i in self.students:
            i.display_info()

tester = StudentManager()
tester.add_student([1, "김철수", 20])
tester.add_student([2, "이영희", 21])
tester.add_student([3, "박지민", 19])

print("현재 등록된 학생 목록:")
tester.display_all_students()
print()

tester.add_student([4, "한지수", 22])
print("학번 4번 학생 추가 후:")
tester.display_all_students()