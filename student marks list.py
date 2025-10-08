class Student:
    def __init__(self, student_roll):
        self.student_roll = student_roll
        self.subjects = []
        self.total = 0
        self.avg = 0

    def input_marks(self):
        print(f"Enter the marks for Student {self.student_roll}:")
        for i in range(1, 4):  # 3 subjects
            mark = float(input(f"  Subject {i}: "))
            self.subjects.append(mark)

    def cal_total(self):
        self.total = sum(self.subjects)
        self.avg = self.total / len(self.subjects)

    def disp_result(self):
        print(f"\nStudent Roll No: {self.student_roll}")
        print(f"  Total Marks: {self.total}")
        print(f"  Average Marks: {self.avg:.2f}")


class StudentGroup:
    def __init__(self, num_students):
        self.students = [Student(i + 1) for i in range(num_students)]

    def process_students(self):
        for student in self.students:
            student.input_marks()
            student.cal_total()

    def show_all_results(self):
        print("\n===== Student Results =====")
        for student in self.students:
            student.disp_result()


# Main program
num = int(input("Enter number of students: "))
group = StudentGroup(num)
group.process_students()
group.show_all_results()
