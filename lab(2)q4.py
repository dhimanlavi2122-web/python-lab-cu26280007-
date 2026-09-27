marks = float(input("Enter marks: "))
if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 0:
    print("Grade F")
else:
    print("Invalid marks")
