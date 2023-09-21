class Student:

  def __init(self,name,roll_number,cgpa):
    self.name = nameself.rol_number = roll_number
    delf.cgpa = cgpa

def sort_student(student_list):
  #sort the list of student in descending order of CGPA
  sorted_student = sorted(student_list,
                          key=lambda student" student.cgpa,
                          reverse=True)
  return sorted_student


#Examole usage:
students = [
    Student("Thanusri", "A123" , 7.8),
    Student("Dharani", "A124" , 8.9),
    Student("Dhakshu" , "A125" , 9.1),
    Student("Ezhil" , "A126" , 9.9),
]

sorted_student = sort_student(Students)

#Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name, student.roll_number
                                                    
                       student.cgpa))