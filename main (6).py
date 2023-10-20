class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  # Syntax - lambda arg:exp
  return sorted_students
students = [
    Student("Sandhiya", "A123", 7.8),
    Student("Kaviya", "A124", 9.2),
    Student("Nivetha", "A125", 9.1),
    Student("Sripriya", "A126", 8.3),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                            student.roll_number,
                            student.cgpa))
