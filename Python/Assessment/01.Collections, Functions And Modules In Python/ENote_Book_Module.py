import os
import logging

def display_menu():
    menu = """
           Press 1. Add Note
           Press 2. View Notes
           Press 3. Exit
            """
    # Display the main menu 
    print()
    print("("*10,"Python E-Note Book",")"*10)
    print(menu)
    
        
def add_note():
    logging.info("\n\n" + "-"*70)
        # get the generator name from user
    generator_name = input("Enter Python E-Note Generator Name : ")
    
        # if user enter nothing in generator name.
    if not generator_name:
        print("Please Enter a Name...!!!")
        logging.error("\nInvalid input for generator name")
        return
    
        # if user enter only Digits in generator name.
    elif generator_name.isdigit():
        print("Error: Invalid Input")
        logging.error("\nInvalid input for generator name")
        return

        # get the note title from the user
    title = input("Enter Python E-Note Title : ")
    
    if not title:
            # if user enter nothing in generator name.
        print("Please Enter a Title...!!!")
        logging.error("\nInvalid input for title")
        return

        # get the note content from the user.
    content = input("Enter E-Note Content : ")
    if not content:
        # Log an error if the input is invalid
        print("Please Enter a Content ...!!!")
        logging.error("Invalid input for content")
        return

        # Create the note string
    fnote = f"\nNote Generator     : {generator_name}\nE-Note Title       : {title}\nE-Note Description : {content}\n"
    note = f"\nE-Note Title : {title}\nE-Note Description : {content}\n\t\t\t Note Generator : {generator_name}\n"
        # Append the note to 'notes.txt'
    with open("notes.txt", "a") as file:
        file.write(fnote + "\n")
        # Log the addition of the note
    logging.info(note)
    print("Note added successfully!")


def view_notes():
    logging.info("\n\n" + "-"*70)
        # Check if 'notes.txt' exists
    if os.path.exists("notes.txt"):
            # Read and display the notes
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            if notes:
                print("\n----------- Your Notes -------------")
                for note in notes:
                    print(note.strip())
                    # Log that notes were viewed
                logging.info("\nViewed notes")
            else:
                print("No notes found.")
                    # Log that no notes were found
                logging.info("\nNo notes found to view")
    else:
        print("No notes found.")
        # Log that the notes file was not found
        logging.info("\nNo notes file found")