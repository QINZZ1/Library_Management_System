
# This function is to allow users to exit to the main menu during another function
def return_opt(user_input):
    if user_input.upper() == 'QUIT': # Checks if user inputs quit
        confirm= input('Are you sure you want to exit to main menu? (y/n): ')
        if confirm.upper() == 'Y':
            print('Returning to Main Menu...')
            return True # User confirms quit, function executes return
        else:
            return False # User cancels quit, continue program
    else:
        return False

def clear():  # Function to clear terminal
    print("\n" * 50)

