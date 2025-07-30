def load_data(file_path):
    with open(file_path, 'r') as file:
        return [line.strip().split(',') for line in file if line.strip()]

def display_member():
    members = load_data("members.txt")
    headers = ["Member ID", "Name", "Contact", "Status"]
    col_widths = [12, 25, 30, 10]

    def format_row(row):
        return "| {0:<12} | {1:<25} | {2:<30} | {3:<10} |".format(*row)

    print("-" * (sum(col_widths) + 13))
    print(format_row(headers))
    print("-" * (sum(col_widths) + 13))

    for member in members:
        print(format_row(member))

    print("-" * (sum(col_widths) + 13))
    input("\nPress Enter to return...")

if __name__ == "__main__":
    display_member()
