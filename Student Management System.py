student = []

n = int(input("Enter Number Of The Students: "))

for i in range(n):
    name = input("\nEnter Name Of The Student: ")

    subs = []
    marks = []

    for j in range(5):
        sub = input(f"Enter Subject Name {j+1}: ")
        subs.append(sub)

        mark = int(input(f"Enter Marks for {sub}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 5

    if average >= 90:
        grade = "A+"
    elif average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"

    student.append([name, subs, marks, total, average, grade])

print("\n---------- REPORT CARD ----------")

for s in student:
    print("\nName :", s[0])

    print("\nSubjects and Marks:")
    for i in range(5):
        print(f"{s[1][i]} : {s[2][i]}")
    print("\nTotal   :", s[3])
    print("Average :", round(s[4], 2))
    print("Grade   :", s[5])