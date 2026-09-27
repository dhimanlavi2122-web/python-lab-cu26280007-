ch = input("enter character:")
if ch.isupper():
    print("uppercase")
elif ch.islower():
    print("lowercase")
elif ch.isdigit():
    print("digit")
else:
    print("special character")