print("WELCOME TO STUDENT REPORT CARD GENERATOR!")

name=input("Enter your name:")
roll=input("Enter your roll no. :")

subjects=["Maths", "Science", "Hindi", "English", "Social Science"]
marks=[]

for subject in subjects:
    score = float(input(f"Enter marks for {subject}: "))
    marks.append(score)
    total = sum(marks)
average = total / len(subjects)

# Grade logic
if average >= 90:
    grade = "A+"
elif average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "F"

print("\n----- Report Card -----")
print(f"Name      : {name}")
print(f"Roll No.  : {roll}")
print(f"Subjects  : {subjects}")
print(f"Marks     : {marks}")
print(f"Total     : {total}")
print(f"Average   : {average:.2f}")
print(f"Grade     : {grade}")
print("------------------------")