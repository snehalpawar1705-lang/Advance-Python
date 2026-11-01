
import csv
import json

# Step 1: Store student details in CSV file
n = int(input("Enter number of students: "))

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Roll_No", "Name", "Branch", "Marks1", "Marks2", "Marks3"])

    for i in range(n):
        print("\nEnter details of student", i + 1)

        roll = input("Roll Number: ")
        name = input("Name: ")
        branch = input("Branch: ")

        m1 = int(input("Marks in Subject 1: "))
        m2 = int(input("Marks in Subject 2: "))
        m3 = int(input("Marks in Subject 3: "))

        writer.writerow([roll, name, branch, m1, m2, m3])

print("\nStudent details saved in CSV file.")

# Step 2: Read CSV and process student records
processed_records = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        m1 = int(row["Marks1"])
        m2 = int(row["Marks2"])
        m3 = int(row["Marks3"])

        total = m1 + m2 + m3
        percentage = total / 3

        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "F"

        record = {
            "Roll_No": row["Roll_No"],
            "Name": row["Name"],
            "Branch": row["Branch"],
            "Total": total,
            "Percentage": round(percentage, 2),
            "Grade": grade
        }

        processed_records.append(record)

# Step 3: Store processed records in JSON file
with open("students.json", "w") as file:
    json.dump(processed_records, file, indent=4)

print("\nProcessed records saved in JSON file.")

# Step 4: Display student results
print("\nStudent Results:")
for student in processed_records:
    print(student)
