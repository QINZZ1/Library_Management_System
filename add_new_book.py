from function import return_opt, clear

def add_new_book(): # Function to add a new book
    clear() #Clears screen
    print("\n--- Add new book ---")
    print("(Enter 'QUIT' at any time to return to menu)")

    while True:  # Loop to obtain book id
        # Takes book ID as input and converts it to name format if not written properly
        bookID = input("Enter book ID (less than 4 digits): ").strip()
        quit_attempt = return_opt(bookID)
        if quit_attempt:  # User confirmed quit
            return
        # User typed quit but cancelled
        elif quit_attempt is False and bookID.upper() == "QUIT":
            continue

        try:
            if len(bookID) > 3 or int(bookID) < 0: #Check length of string then convert to int for value check
                print("Ensure your book ID is less than 4 digits (e.g. 123")
                continue

        except ValueError:
            print("Error! Enter a proper book ID")
            continue

        exist_bookID = False
        try:
            with open("books.txt", "r") as file:
                file.readline() #read and discard the header
                for line in file:
                    parts = line.strip().split(',')
                    if parts:
                        file_book_id = parts[0] #Get bookID from file line
                        if bookID == file_book_id: #Compare user input with bookID
                            exist_bookID = True
                            break #Found match, exit loop
        except FileNotFoundError:
            print(f"The file 'books.txt' was not found")

        if exist_bookID:
            print(f"BookID: {bookID} already exists.")
            continue # Go back start of the loop
        else:
            # If we reach here, the bookID is valid in format AND unique
            print(f"BookID: {bookID} is unique. Proceeding to add book title...")
            break


    while True: #Loop to obtain book title
        book_title = input("Enter book title: ").title()
        quit_attempt = return_opt(book_title)
        if quit_attempt:
            return
        elif quit_attempt is False and book_title.upper() == "QUIT":
            continue

        if not book_title: #Check if input is empty
            print("ERROR!, Book title cannot be empty, try again. ")
        else:
            break


    while True: #Loop to obtain book author
        book_author = input("Enter book author: ").title()
        quit_attempt = return_opt(book_author)
        if quit_attempt:
            return
        elif quit_attempt is False and book_author.upper() == "QUIT":
            continue

        if not book_author:  # Check if input is empty
            print("ERROR!, Book author cannot be empty, try again. ")
        else:
            break

    while True:# Loop to obtain book availablity status
        book_availability = input("Enter book availability (Available / Borrowed): ").title().strip()
        quit_attempt = return_opt(book_availability)
        if quit_attempt:
            return
        elif quit_attempt is False and book_availability.upper() == "QUIT":
            continue

        if book_availability in ["Available", "Borrowed"]:
            break
        else:
            print("Error Availability status. Enter 'Available' or 'Borrowed'.")


    with open ("books.txt","a") as file: #Add new book to books.txt
        file.write(f'{bookID},{book_title},{book_author},{book_availability}\n')

    print("\nBook Registered Successfully.")
    input("Press Enter to return to main menu...")
