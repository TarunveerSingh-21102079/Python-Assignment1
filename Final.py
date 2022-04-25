# Question1

NUM1 = float(input("Enter First Number : "))
NUM2 = float(input("Enter Second Number : "))
NUM3 = float(input("Enter Third Number : "))
AVG = (NUM1 + NUM2 + NUM3)/3
print("Average of three number is : ", AVG)

# Question2

G_I = float(input("Enter the Gross Income : "))
D = float(input("Enter Dependent : "))
S_D = 10000
D_D_A = D * 3000
Taxable_Income = G_I - S_D - D_D_A
TAX = float((20 / 100) * (Taxable_Income))  # Tax is 20% of Taxable_Income
print("Your income tax : ", TAX)

# Question3

SID = int(input("Enter SID:"))
NAME = str(input("Enter Name:"))

GENDER = str(input("Enter Gender:"))

COURSE_NAME = input("Enter Course Name:")
CGPA = float(input("Enter CGPA"))

LIST = [SID, NAME, GENDER, COURSE_NAME, CGPA]
print(LIST)

# Question4

MARKS_1 = int(input('marks of studentA: '))
MARKS_2 = int(input('marks of studentB: '))
MARKS_2 = int(input('marks of studentC: '))
MARKS_4 = int(input('marks of studentD: '))
MARKS_5 = int(input('marks of studentE: '))
list = [MARKS_1, MARKS_2, MARKS_3, MARKS_4, MARKS_5]
SORTED_LIST = list.sort()
print("Sorted marks of students is:",SORTED_LIST)

# question 5a

color=['red','Green', "White",'Black', 'Pink', 'Yellow']
color.pop(3)
print(color)

# question 5b

color=['red','Green', "White",'Black', 'Pink', 'Yellow']
color[2:4] = ['Purple']
print(color)
