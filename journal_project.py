import os
from datetime import datetime

class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def read_entries(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            content = file.read()
        return [entry for entry in content.strip().split("\n\n") if entry.strip()]

    def add_entry(self):
        text = input("\nEnter your journal entry: ").strip()
        if not text:
            print("Entry cannot be empty.")
            return
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}]\n{text}\n\n"
 
        try:
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(entry)
                    
            print("\nEntry added successfully!")
        except PermissionError:
                print("Error: Permission denied while writing to the journal file.")
                
        except OSError as error:
            print(f"File error: {error}")

    def view_entries(self):
        try:
            entries = self.read_entries()
            if not entries:
                print("\nNo journal entries found. Start by adding a new entry!")
                return
            print("\nYour Journal Entries:")
            print("-" * 40)
            for entry in entries:
                print(entry)
                print()
        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Error: Permission denied while reading the journal file.")
        except OSError as error:
            print(f"File error: {error}")

    def search_entries(self):
        keyword = input("\nEnter a keyword or date to search: ").strip()
        if not keyword:
            print("Search text cannot be empty.")
            return
        try:
            entries = self.read_entries()
            matches = [entry for entry in entries if keyword.casefold() in entry.casefold()]
            if not matches:
                print(f"\nNo entries were found for the keyword: {keyword}.")
                return
            print("\nMatching Entries:")
            print("-" * 40)
            for entry in matches:
                print(entry)
                print()
        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Error: Permission denied while searching the journal file.")
        except OSError as error:
            print(f"File error: {error}")

    def delete_entries(self):
        if not os.path.exists(self.filename):
            print("\nNo journal entries to delete.")
            return
        confirm = input("\nAre you sure you want to delete all entries? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("Deletion cancelled. Your entries are safe.")
            return
        try:
            os.remove(self.filename)
            print("\nAll journal entries have been deleted.")
        
        except FileNotFoundError:
            print("\nNo journal entries to delete.")
            
        except PermissionError:
            print("Error: Permission denied while deleting journal entries.")
            
        except OSError as error:
            print(f"File error: {error}")

def main():
    journal = JournalManager()
    print("\nWelcome to Personal Journal Manager!")
    while True:
        print("\nPlease select an option:")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")
        try:
            choice = input("\nEnter your choice: ").strip()
            match choice:
                case "1":
                    journal.add_entry()
                case "2":
                    journal.view_entries()
                case "3":
                    journal.search_entries()
                case "4":
                    journal.delete_entries()
                case "5":
                    print("\nThank you for using Personal Journal Manager. Goodbye!")
                    break
                case _:
                    print("\nInvalid option. Please select a valid option from the menu.")
        except (KeyboardInterrupt, EOFError):
            print("\nProgram terminated.")
            break

if __name__ == "__main__":
    main()