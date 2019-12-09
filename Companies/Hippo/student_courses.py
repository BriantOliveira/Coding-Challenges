# Your previous work is preserved below: 
# 
# /*
# 
# You are a developer for a university. Your current project is to develop a system for students to find courses they share with friends. The university has a system for querying courses students are enrolled in, returned as a list of (ID, course) pairs.
# 
# Write a function that takes in a list of (student ID number, course name) pairs and returns, for every pair of students, a list of all courses they share.
# 
# Sample Input:
# 
# student_course_pairs_1 = [
#   ["58", "Linear Algebra"],
#   ["94", "Art History"],
#   ["94", "Operating Systems"],
#   ["17", "Software Design"],
#   ["58", "Mechanics"],
#   ["58", "Economics"],
#   ["17", "Linear Algebra"],
#   ["17", "Political Science"],
#   ["94", "Economics"],
#   ["25", "Economics"],
#   ["58", "Software Design"],
# 
# ]
# 
# Sample Output (pseudocode, in any order):
# 
# find_pairs(student_course_pairs_1) =>
# {
#   [58, 17]: ["Software Design", "Linear Algebra"]
#   [58, 94]: ["Economics"]
#   [58, 25]: ["Economics"]
#   [94, 25]: ["Economics"]
#   [17, 94]: []
#   [17, 25]: []
# }
# 
# Additional test cases:
# 
# Sample Input:
# 
# student_course_pairs_2 = [
#   ["42", "Software Design"],
#   ["0", "Advanced Mechanics"],
#   ["9", "Art History"],
# ]
# 
# Sample output:
# 
# find_pairs(student_course_pairs_2) =>
# {
#   [0, 42]: []
#   [0, 9]: []
#   [9, 42]: []
# }
# 
# 
# 
# */
# 
# const studentCoursePairs1 = [
#   ["58", "Linear Algebra"],
#   ["94", "Art History"],
#   ["94", "Operating Systems"],
#   ["17", "Software Design"],
#   ["58", "Mechanics"],
#   ["58", "Economics"],
#   ["17", "Linear Algebra"],
#   ["17", "Political Science"],
#   ["94", "Economics"],
#   ["25", "Economics"],
#   ["58", "Software Design"]
# 
# ];
# 
# const studentCoursePairs2 = [
#   ["42", "Software Design"],
#   ["0", "Advanced Mechanics"],
#   ["9", "Art History"],
# ];
# 
# 
# {
#   "Linear Algebra": [58, 17],
#   "Economics": [58, 94, 25]
# }
# 
# 
# 
# function studentCoursePairs(studentCoursePairs1) {
#   coursesInCommon = []
#   
#   for (var i = 0; i < studentCoursePairs1.length; i++){
#     
#     var studentsIds = studentCoursePairs1
#   }
# }

student_course_pairs_1 = [
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
  ["58", "Software Design"],

]

student_course_pairs_2 = [
  ["42", "Software Design"],
  ["0", "Advanced Mechanics"],
  ["9", "Art History"],
]

'''

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

'''

import itertools

def find_pars(student_courses):
    courses_dict = {}
    students_list = []
    
    for i in range(len(student_courses)):
        students_id = student_courses[i][0]
        courses = student_courses[i][1]

        if courses not in courses_dict:            
            courses_dict[courses] = [students_id]
            students_list.append(students_id)

        else:
            courses_dict.setdefault(courses,[]).append(students_id)
            students_list.append(students_id)

    return courses_dict, students_list

def find_the_not_pairs():
    courses_dict = find_pars(student_course_pairs_1)
    student_pairs_dict = {}
    studentsIds = courses_dict[1]
    courses = courses_dict[0].keys()
    # print(courses_dict[0].keys())
    for pair in itertools.combinations(studentsIds, 2):
      student_pairs = pair
      # print(student_pairs)
      if student_pairs in student_pairs_dict:
        students = [student_pairs[0], student_pairs[1]]
        if students in courses_dict[0].values():
            print(students)
            
          
          # student_pairs_dict.setdefault(pair,[]).append(courses_dict[0].keys())
  
      student_pairs_dict[pair] = []
    # print(student_pairs_dict)
     
    # print(student_pairs_dict)
      


       
      # print(ids)