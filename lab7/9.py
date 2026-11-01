import csv
import glob
def program_9():
    source_name = input("Enter the source file name: ")
    destination_name = input("Enter the destination file name: ")

    with open(source_name, "r", encoding="utf-8") as source:
        content = source.read()

    with open(destination_name, "w", encoding="utf-8") as destination:
        destination.write(content)

    print("File copied successfully.")

