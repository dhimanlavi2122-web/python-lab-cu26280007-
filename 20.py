marks =[]
for i in range(5):
    marks.append (float(input("enter marks:")))
    percentage = sum(marks) /5
    print("percentage=", percentage, "%")