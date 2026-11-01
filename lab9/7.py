books = []

while True:
    print("\n1. Add book  2. View books  3. Update book  4. Delete book  0. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        book_id = input("Book ID: ")
        title = input("Title: ")
        author = input("Author: ")
        books.append({"id": book_id, "title": title, "author": author})
        print("Book added.")

    elif choice == "2":
        for book in books:
            print(book)

    elif choice == "3":
        book_id = input("Book ID to update: ")
        book = next((b for b in books if b["id"] == book_id), None)
        if book:
            book["title"] = input("New title: ")
            book["author"] = input("New author: ")
            print("Book updated.")
        else:
            print("Book not found.")

    elif choice == "4":
        book_id = input("Book ID to delete: ")
        old_count = len(books)
        books = [b for b in books if b["id"] != book_id]
        print("Book deleted." if len(books) < old_count else "Book not found.")

    elif choice == "0":
        break

    else:
        print("Invalid choice.")