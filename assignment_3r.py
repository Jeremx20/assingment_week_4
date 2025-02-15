'''

For this assignment please do the following:

- Read in the student_grades.csv file

- calculate the average grade for the class

- for each student record calculate the difference between the student's grade and the average grade

- write the output to a new file called student_grade_differences.csv

'''
with open('student_grades.csv', 'r') as f:
    lines = f.readlines()

if len(lines) > 0:  
    grades = []

    for line in lines[1:]:
        row = line.strip().split(',')
        grades.append(float(row[3]))  

    
    avg = sum(grades) / len(grades)

    
    with open('student_grade_differences.csv', 'w') as f_out:
        f_out.write("id,first_name,last_name,grade,difference_from_avg\n")

        for line in lines[1:]:  
            row = line.strip().split(',')
            grade = float(row[3])
            difference = grade - avg
            f_out.write(f"{row[0]},{row[1]},{row[2]},{grade},{difference:.2f}\n")

