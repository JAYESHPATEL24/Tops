import os
import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def display_menu():
    print("\n--- Python E-Note Book ---")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

def add_note():
    generator_name = input("Enter Python E-Note Generator Name: ").strip()
    if not generator_name:
        print("Error: Invalid Input")
        logging.error("Invalid input for generator name")
        return

    title = input("Enter Python E-Note Title: ").strip()
    if not title:
        print("Error: Invalid Input")
        logging.error("Invalid input for title")
        return

    content = input("Enter E-Note Content: ").strip()
    if not content:
        print("Error: Invalid Input")
        logging.error("Invalid input for content")
        return

    note = f"Generator: {generator_name}\nTitle: {title}\nContent: {content}\n"
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    logging.info("Note added: %s", note)
    print("Note added successfully!")

def view_notes():
    if os.path.exists("notes.txt"):
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            if notes:
                print("\n--- Your Notes ---")
                for note in notes:
                    print(note.strip())
                logging.info("Viewed notes")
            else:
                print("No notes found.")
                logging.info("No notes found to view")
    else:
        print("No notes found.")
        logging.info("No notes file found")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
