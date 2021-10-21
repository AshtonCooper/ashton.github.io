print('RELI 4103 - Perspectives in Catholic Theology')
print('ENTER AS PERCENTAGE!')

Exam_1 = 99.0
Exam_2 = 96.0
Exam_3 = float(input('Exam 3 grade: '))
Paper_1 = 100*34.0
Paper_2 = float(input('Paper 2 grade: '))
Weekly = float(input('Weekly responses grade: '))
Grade = (100.0 * (Exam_1+Exam_2)/2.0 + 50.0 * Exam_3 + Paper_1 + 40.0 * Paper_2 + 75.0 * Weekly)/300.0
print('Numerical grade: ' + str(Grade) + '%')
if Grade > 93.0:
    Letter_grade = 'A'
    GPA = 4.0
elif Grade > 89.0:
    Letter_grade = 'A-'
    GPA = 3.7
elif Grade > 86.0:
    Letter_grade = 'B+'
    GPA = 3.3
elif Grade > 83.0:
    Letter_grade = 'B'
    GPA = 3.0
elif Grade > 79.0:
    Letter_grade = 'B-'
    GPA = 2.7
elif Grade > 76.0:
    Letter_grade = 'C+'
    GPA = 2.3
elif Grade > 73.0:
    Letter_grade = 'C'
    GPA = 2.00
elif Grade > 69.0:
    Letter_grade = 'C-'
    GPA = 1.70
elif Grade > 64.5:
    Letter_grade = 'D'
    GPA = 1.00
else:
    Letter_grade = 'F'
    GPA = 0.00
print('Letter grade: ' + str(Letter_grade))
print('GPA: ' + str(GPA))