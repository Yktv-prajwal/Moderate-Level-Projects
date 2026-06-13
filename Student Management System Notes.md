# 🎓 Student Report Card Management System

## 📌 Project Overview
This Python program is a simple Student Report Card Management System. It allows the user to enter details for multiple students, including their subjects and marks. The program calculates the total marks, average percentage, assigns a grade, and displays a formatted report card for each student.

## 🚀 Features
- Accepts details for multiple students.
- Stores names, subjects, and marks.
- Calculates total and average marks.
- Assigns grades based on average marks.
- Displays a structured report card.
- Beginner-friendly Python project.

## 📚 Concepts Used
- User Input (`input()`)
- Type Casting (`int()`)
- Variables
- Lists and Nested Lists
- Loops (`for`)
- Conditional Statements (`if-elif-else`)
- Built-in Functions (`sum()`, `round()`)
- Basic Data Management

## 🔍 Working of the Program

### Step 1: Enter Student Details
The user enters the number of students whose report cards need to be generated.

### Step 2: Input Subjects and Marks
For each student:
- Enter the student's name.
- Enter five subject names.
- Enter the corresponding marks for each subject.

### Step 3: Calculate Total and Average
The program:
- Calculates the total marks using `sum()`.
- Computes the average marks by dividing the total by the number of subjects.

### Step 4: Assign Grade
The grade is assigned based on the average marks:

| Average Marks | Grade |
|--------------|-------|
| 90 and above | A+ |
| 75 - 89 | A |
| 60 - 74 | B |
| 40 - 59 | C |
| Below 40 | Fail |

### Step 5: Store Student Data
The student's information, including subjects, marks, total, average, and grade, is stored in a nested list.

### Step 6: Display Report Card
The program prints a report card for each student containing:
- Student Name
- Subject-wise Marks
- Total Marks
- Average Marks
- Final Grade

## 💻 Sample Output

```
Enter Number Of The Students: 1

Enter Name Of The Student: Rahul

Enter Subject Name 1: Math
Enter Marks for Math: 90

Enter Subject Name 2: Science
Enter Marks for Science: 85

Enter Subject Name 3: English
Enter Marks for English: 88

Enter Subject Name 4: History
Enter Marks for History: 80

Enter Subject Name 5: Computer
Enter Marks for Computer: 95

---------- REPORT CARD ----------

Name : Rahul

Subjects and Marks:
Math : 90
Science : 85
English : 88
History : 80
Computer : 95

Total   : 438
Average : 87.6
Grade   : A
```

## 🎯 Learning Outcomes
By building this project, I learned:
- Working with nested lists.
- Using loops for repetitive tasks.
- Taking and managing user input.
- Using built-in functions like `sum()` and `round()`.
- Applying conditional statements for grading.
- Organizing and displaying structured data.

## 🔮 Future Improvements
- Allow any number of subjects instead of a fixed five.
- Calculate percentage along with grades.
- Add Pass/Fail status for individual subjects.
- Store student records in a file for future use.
- Search, update, and delete student records.
- Display the highest and lowest scoring students.
- Build a graphical user interface (GUI).

This project is part of my Python learning journey and helps me strengthen my understanding of programming fundamentals, data structures, and problem-solving skills.
