print("========== Grade Checker Program ==========")

num_students = int(input("Enter number of students: "))

for student in range(1, num_students + 1):

    print(f"\nStudent {student}")

    while True:
        marks = float(input("Enter marks (0-100): "))

        if 0 <= marks <= 100:
            break
        else:
            print("Invalid marks! Please enter marks between 0 and 100.")

    if marks >= 90:
        print("Grade: A+")
    elif marks >= 80:
        print("Grade: A")
    elif marks >= 70:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 50:
        print("Grade: D")
    else:
        print("Grade: F")

print("\nGrade checking completed for all students.")

