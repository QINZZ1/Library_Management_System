import re
from function import return_opt, clear

def add_member(): # Function to add a new member
    clear() #Clears screen
    print("\n--- Register New Member ---")
    print("(Enter 'QUIT' at any time to return to menu)")

    while True: # Loop to obtain name
        # Takes name as input and converts it to name format if not written properly
        name=input("Name: ").title().strip()
        quit_attempt = return_opt(name)
        if quit_attempt:  # User confirmed quit
            return
        # User typed quit but cancelled
        elif quit_attempt is False and name.upper() == "QUIT":
            continue
        # Checks if input only consist of alphabets and space
        if all(c.isalpha() or c.isspace() for c in name):
            break
        else:
            print("Invalid Name. Please try again.")

    while True:  # Loop to obtain ID/IC number
        # Takes IC as input & remove spaces
        ic = input("Enter IC Number (e.g., 990101-14-1234): ").strip()
        quit_attempt = return_opt(ic)
        if quit_attempt:
            return
        elif quit_attempt is False and ic.upper() == "QUIT":
            continue
        if re.match(r'^\d{6}-\d{2}-\d{4}$', ic):  # Validate IC format
            break
        else:
            print("Invalid ID format. Please use this format: YYMMDD-XX-XXXX")

    while True: # Loop to obtain phone number
        # Takes number as input & remove spaces
        number=input("Phone Number (e.g., 012-3456789): ").strip()
        quit_attempt = return_opt(number)
        if quit_attempt:
            return
        elif quit_attempt is False and number.upper() == "QUIT":
            continue
        if re.match(r'^(01)[0-9]-\d{7,8}$', number): # Validate Malaysian phone number format
            break
        else:
            print("Invalid Phone Number. Please use this format 012-3456789.")
    while True: # Loop to obtain email address
        email=input("Email Address: ").strip()
        quit_attempt = return_opt(email)
        if quit_attempt:
            return
        elif quit_attempt is False and email.upper() == "QUIT":
            continue
        if re.match(r'^[\w.-]+@[\w.-]+\.\w{2,}$', email): # Validate Email format
            break
        else:
            print("Invalid Email. Please enter a valid email address.")

    # To assign a member ID to new member
    try:
         with open("members.txt","r") as file:
             lines=file.readlines() # Determine how many lines in database
             last_no = len(lines) - 1  # Excluding header
    except FileNotFoundError:
        last_no = 0
    member_no=last_no +1
    member_id=str(member_no+10000)
 
    # To add new member data into database
    with open("members.txt","a") as file:
        file.write(f'{member_no},{member_id},{name},{ic},{number},{email},{'Active'}\n')

    print("\nMember Registered Successfully." )
    input("Press Enter to return to main menu...")




















