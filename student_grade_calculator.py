
print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")

subjects = [
    "Tamil",
    "English",
    "Python",
    "Computer Science",
    "Mathematics"
]

marks = []

for subject in subjects:
    while True:
        try:
            mark = float(input("Enter " + subject + " Mark: "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Enter marks between 0 and 100.")
        except ValueError:
            print("Enter a valid number.")

total = sum(marks)
average = total / 5
percentage = (total / 500) * 100

if any(mark < 35 for mark in marks):
    grade = "F"
    result = "FAIL"
elif average >= 90:
    grade = "A+"
    result = "PASS"
elif average >= 80:
    grade = "A"
    result = "PASS"
elif average >= 70:
    grade = "B"
    result = "PASS"
elif average >= 60:
    grade = "C"
    result = "PASS"
elif average >= 50:
    grade = "D"
    result = "PASS"
else:
    grade = "E"
    result = "PASS"

print("\n===== STUDENT MARKSHEET =====")
print("Student Name:", name)
print("Roll Number:", roll_number)

for i in range(len(subjects)):
    print(subjects[i], ":", marks[i])

print("Total Marks:", total, "/ 500")
print("Average:", round(average, 2))
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Result:", result)

print("==============================")
