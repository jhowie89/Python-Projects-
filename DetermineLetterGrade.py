'''

Determine Letter Grade problem

 

'''

def get_letter_grade(avg):

    if avg >= 90:

        return 'A'

    elif avg >= 80:

        return 'B'

    elif avg >= 70:

        return 'C'

    elif avg >= 60:

        return 'D'

    else:

        return 'F'

 

# Initialize arrays

Names = []

Tests = []

LetterGrades = []

 

# Number of students

num_students = 5

 

# Input data from user

for i in range(num_students):

    print(f"\nEnter data for student {i+1}:")

    name = input("Name: ")

    test1 = float(input("Test 1 score: "))

    test2 = float(input("Test 2 score: "))

    midterm = float(input("Midterm Exam score: "))

    final = float(input("Final Exam score: "))

 

    # Store name

    Names.append(name)

 

    # Calculate average

    semester_avg = (test1 + test2 + midterm + final) / 4

    Tests.append([test1, test2, midterm, final, semester_avg])

 

    # Determine letter grade

    letter = get_letter_grade(semester_avg)

    LetterGrades.append(letter)

 

# Print the grade book

print("\n{:<20} {:<8} {:<8} {:<13} {:<11} {:<18} {:<17}".format(

    "Name", "Test 1", "Test 2", "Midterm Exam", "Final Exam", "Semester Average", "Letter Grade"

))

print("-" * 95)

 

for i in range(num_students):

    print("{:<20} {:<8} {:<8} {:<13} {:<11} {:<18.2f} {:<17}".format(

        Names[i],

        Tests[i][0],

        Tests[i][1],

        Tests[i][2],

        Tests[i][3],

        Tests[i][4],

        LetterGrades[i]

    ))