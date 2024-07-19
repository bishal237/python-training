import csv

absent_students = []
present_students = []

with open("data.csv") as f:
    reader = csv.DictReader(f)
#     #reader = csv.reader(f)
    for row in reader:
        
        print(row)
        if row['attendence'] == 'A':
            absent_students.append((row['students_name'], row['date']))
        elif row['attendence'] == 'p':
            present_students.append((row['students_name'],row['date']))


print("Absent_students:")
for student_name in absent_students:
    print(f"Name:{student_name[0]}, Date:{student_name[1]}")

print("\nPresent Student:")
for students_name in present_students:
    print(f"Name:{student_name[0]}, Date:{student_name[1]}")
    


with open('absent_students.csv', 'w', newline = '', encoding='data.csv') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['students_name', 'date', 'attendence'])
    for students in present_students:
        writer.writerow([students[0],students[1]], 'A')
        
with open('present_students.csv', 'w', newline = '', encoding='data.csv') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['students_name', 'date', 'attendence'])
    for students in present_students:
        writer.writerow([students[0],students[1]], 'P')
                
        