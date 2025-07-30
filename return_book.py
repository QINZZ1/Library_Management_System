from datetime import datetime
from function import clear, return_opt
import csv

def return_book():
    while True:  # Outer loop to retry the return process
        clear()
        print("\n--- Return a Book ---")
        print("(Enter 'QUIT' at any time to return to main menu)")

        # Input Book ID
        while True:
            book_id = input("Enter Book ID to return: ").strip()
            if return_opt(book_id): return
            if book_id.isdigit() and len(book_id) == 3:
                break
            else:
                print("Invalid Book ID. Please enter a valid numeric ID (exactly 3 digits).")

        # Input Member ID
        while True:
            member_id = input("Enter Member ID: ").strip()
            if return_opt(member_id): return
            if member_id.isdigit() and len(member_id) == 5:
                break
            else:
                print("Invalid Member ID. Please enter a valid numeric ID (exactly 5 digits).")

        # Update lending.txt
        try:
            with open("lending.txt", "r", encoding="utf-8") as file:
                lines = [line.strip() for line in file.readlines() if line.strip()]

            if len(lines) < 2:
                print("⚠️ lending.txt is empty or has no records.")
                input("Press Enter to retry...")
                continue

            header = lines[0]
            records = lines[1:]
            updated_records = []
            found = False
            return_date = datetime.today().strftime("%Y-%m-%d")

            for line in records:
                parts = line.strip().split(",")
                if len(parts) < 4:
                    updated_records.append(line + "\n")
                    continue

                l_book_id, l_member_id, lend_date, r_date = parts
                if l_book_id == book_id and l_member_id == member_id and r_date.strip() == "":
                    updated_line = f"{l_book_id},{l_member_id},{lend_date},{return_date}\n"
                    updated_records.append(updated_line)
                    found = True
                else:
                    updated_records.append(line + ("\n" if not line.endswith("\n") else ""))

            if not found:
                print("\n❌ No active lending record found for this Book ID and Member ID.")
                input("Press Enter to try again...")
                continue  # Stay in return flow

            with open("lending.txt", "w", encoding="utf-8") as file:
                file.write(header + "\n")
                file.writelines(updated_records)

            print(f"\n✅ Book ID {book_id} returned by Member ID {member_id} on {return_date}.")

        except FileNotFoundError:
            print("❌ lending.txt not found. Make sure the file exists.")
            input("Press Enter to try again...")
            continue

        # Update books.txt
        try:
            books = []
            found_book = False

            with open("books.txt", "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["Book ID"].strip() == book_id and row["Availability"].strip().lower() == "borrowed":
                        row["Availability"] = "Available"
                        found_book = True
                    books.append(row)

            if not found_book:
                print("⚠️ Book was not marked as 'Borrowed' or not found in books.txt.")
            else:
                with open("books.txt", "w", newline='', encoding="utf-8") as file:
                    fieldnames = ["Book ID", "Title", "Author", "Availability"]
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(books)
                print("✅ Book availability updated in books.txt.")

            input("\nPress Enter to return to the main menu...")
            break  # Exit loop after successful return

        except FileNotFoundError:
            print("⚠️ books.txt not found. Book availability could not be updated.")
            input("Press Enter to return to the main menu...")
            return
