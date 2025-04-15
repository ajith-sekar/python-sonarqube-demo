import json
import os

BOOKS_FILE = "books.json"

def load_books():
    if not os.path.exists(BOOKS_FILE):
        return []
    with open(BOOKS_FILE, "r") as file:
        return json.load(file)

def save_books(books):
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)

def add_book(title, author):
    books = load_books()
    books.append({"title": title, "author": author})
    save_books(books)
    print(f"Book '{title}' by {author} added.")

def list_books():
    books = load_books()
    if not books:
        print("No books found.")
        return
    print("\nList of Books:")
    for index, book in enumerate(books, 1):
        print(f"{index}. {book['title']} by {book['author']}")

def search_books(keyword):
    books = load_books()
    found = [book for book in books if keyword.lower() in book['title'].lower() or keyword.lower() in book['author'].lower()]
    if not found:
        print("No matching books found.")
    else:
        print("\nSearch Results:")
        for book in found:
            print(f"{book['title']} by {book['author']}")

def delete_book(index):
    books = load_books()
    try:
        removed = books.pop(index - 1)
        save_books(books)
        print(f"Removed book: {removed['title']} by {removed['author']}")
    except IndexError:
        print("Invalid index. No book deleted.")

def main():
    while True:
        print("\n=== Book Manager ===")
        print("1. Add Book")
        print("2. List Books")
        print("3. Search Books")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            add_book(title, author)
        elif choice == "2":
            list_books()
        elif choice == "3":
            keyword = input("Enter keyword to search: ")
            search_books(keyword)
        elif choice == "4":
            list_books()
            try:
                index = int(input("Enter the book number to delete: "))
                delete_book(index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
