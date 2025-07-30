
def load_data(file_path): # Load data from a file and return it as a list of lists
    with open(file_path, 'r') as file:
        return [line.strip().split(',') for line in file if line.strip()]

def display_inventory(): # Function to display members and their information
    books = load_data("books.txt") # Loads data from books.txt
    headers = ["Book ID", "Title", "Author", "Status"]
    col_widths = [10, 35, 25, 10]

    def format_row(row): # Function to display books inventory as a table
        return "| {0:<10} | {1:<35} | {2:<25} | {3:<10} |".format(*row)

    print("-" * (sum(col_widths) + 13))
    print(format_row(headers))
    print("-" * (sum(col_widths) + 13))

    for book in books:
        print(format_row(book))

    print("-" * (sum(col_widths) + 13))
    input("\nPress Enter to return...")

if __name__ == "__main__":
    display_inventory()


