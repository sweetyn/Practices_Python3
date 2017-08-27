"""Generate Test data for below function
Grade(Obtained marks, Total marks) having below grading system."""


def markGrade(obtainMarks, totalMarks):
    gradeVal = 0

    gradeVal = 100 * (obtainMarks/totalMarks)
    # print(gradeVal)
    if gradeVal >= 0 and gradeVal <= 40:
        grade = 'D'
    elif gradeVal >= 41 and gradeVal <= 60:
        grade = 'C'
    elif gradeVal >= 61 and gradeVal <= 80:
        grade = 'B'
    elif gradeVal >= 81 and gradeVal <= 100:
        grade = 'A'

    return grade

obtainMarks = 20
totalMarks = 40
grade=''

print('Grading calculation = Grade (', obtainMarks, ',', totalMarks, ') = ')
print(markGrade(obtainMarks, totalMarks),'grade')
