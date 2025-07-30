from function import return_opt, clear
import csv
import time

def load_books(): #function to load the book list
    books = []
    with open('books.txt', 'r') as file:
        reader = csv.DictReader(file) # Create a CSV dictionary reader to read each row as a dictionary
        for book in reader: # Loop through each book record in the file
            book['Book ID'] = int(book['Book ID'])  # Ensure ID is int
            books.append(book) # Add the processed book record to the books list
    return books

def load_members():
    members = []
    with open('members.txt', 'r') as file:
        reader = csv.DictReader(file) # Create a CSV dictionary reader to read each row as a dictionary
        for member in reader: # Loop through each member record in the file
            member['Member ID'] = int(member['Member ID'])  # Ensure ID is int
            members.append(member) # Add the processed member record to the members list
    return members

def lend_book(books, members): #function to lend a book
    clear() #clear the screen
    print("\n--- Lending Book ---")
    print(f'(Enter \'QUIT\' at any time to return to main menu)')

    # Ask for Book ID
    while True:
        book_id = input('Book ID: ').strip()
        quit_attempt = return_opt(book_id)
        if quit_attempt: #user confirmed quit
            return
        #user typped quit but cancelled
        elif quit_attempt is False and book_id.upper() == "QUIT":
            continue
        #to validate the inputs
        try:
            book_id = int(book_id)
        except ValueError:
            print('Error: Book ID must be a number.')
            continue
        #to check for book availability
        book_found = False
        for b in books:
            if b['Book ID'] == book_id:
                book_found = True
                if b['Availability'] != "Available":
                    print(f'Sorry, book {b["Book ID"]} is already borrowed. Please enter another book.')
                    break  # Break out of for, not the outer while
                else:
                    break  # Valid book found and available
        if not book_found:
            print('Error: Book ID not found.')
            continue #ask for book id again
        if book_found and b['Availability'] == "Available":
            break  # Exit input loop when valid & available book is found

    # Ask for Member ID
    while True:
        member_id = input('Member ID: ').strip()
        quit_attempt = return_opt(member_id)
        if quit_attempt: #user confirmed quit
            return
        #user typped quit but cancelled
        elif quit_attempt is False and member_id.upper() == "QUIT":
            continue
        #to validate the input
        try:
            member_id = int(member_id)
        except ValueError:
            print('Error: Member ID must be a number.')
            continue
        #to check for member's status
        member_found = False
        active_member = False
        for m in members:
            if m['Member ID'] == member_id:
                member_found = True
                if m['Status'] == 'Active':
                    active_member = True
                break
        #the case when member id is not found
        if not member_found:
            print(f'Member ID {member_id} not found.')
            continue
        if not active_member:
            print(f'Member ID {member_id} is not active.')
            return
        break

    # Update book status
    b['Availability'] = "Borrowed"
    lending_date = time.strftime('%Y-%m-%d')
    #append the lending record to the lending.txt
    with open('lending.txt', 'a') as lending_file:
        # Format: Book ID, Member ID, Lending Date
        lending_file.write(f'{book_id},{member_id},{lending_date},\n')

        # Save updated books to books.txt
    with open('books.txt', 'w', newline='') as file:
        # Define the field names (columns) for the CSV file
        fieldnames = ['Book ID', 'Title', 'Author', 'Availability']
        # Create a CSV DictWriter object using the defined fieldnames
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # Write the header row (column titles) to the file
        writer.writeheader()
        for book in books:
            # Only keep allowed fields
            filtered_book = {key: book[key] for key in fieldnames}
            filtered_book['Book ID'] = str(filtered_book['Book ID'])  # Ensure Book ID is a string
            writer.writerow(filtered_book)

    # Confirm success
    print(f'"{b["Title"]}" (Book ID {book_id}) has been borrowed by {m["Member Name"]} (Member ID {member_id}).')
    input("Press Enter to return to the main menu...")

def lending():
    books = load_books()
    members = load_members()
    lend_book(books, members)
