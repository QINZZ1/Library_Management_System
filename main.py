import add_member,add_new_book,return_book,lend_book,display_book_inventory,display_member_information
from function import clear

def main():
    while True:
        clear()  # Clears the terminal screen
        print("📚" * 25)
        print("     📖 WELCOME TO THE LIBRARY MANAGEMENT SYSTEM 📖     ")
        print("📚" * 25)
        print("\nPlease select an option below:\n")
        print("  1️⃣  Add New Book 📘")
        print("  2️⃣  Register New Member 🧑‍💼")
        print("  3️⃣  Lend a Book 📥")
        print("  4️⃣  Return a Book 📤")
        print("  5️⃣  Display Book Inventory 📚")
        print("  6️⃣  Display Member Information 👥")
        print("  7️⃣  Exit 🚪")
        print("\n" + "-" * 50)

        choice = input("Enter your choice (1-7): ").strip()

        match choice:
            case '1':
                add_new_book.add_new_book()
            case '2':
                add_member.add_member()
            case '3':
               lend_book.lending()
            case '4':
                return_book.return_book()
            case '5':
                display_book_inventory.display_inventory()
            case '6':
                display_member_information.display_member()
            case '7':
                print("Exiting program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 7.")
                input("Press Enter to continue...")

main()


