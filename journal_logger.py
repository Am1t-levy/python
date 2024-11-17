from datetime import datetime 

def log_entry():

    with open('journal.txt', 'a') as file:
        while True:
            entry = input("Enter your journal entry (or type 'exit' to finish): ")
            if entry.lower() == 'exit':
                break
            timestamp = datetime.now().strftime("[%Y-%D %H:%M:%S]")
            file.write(f"{timestamp} {entry}\n")
            print("Entry logged!")
    
    with open('journal.txt', 'r') as file:
        print("\ncontents of journal.txt:")
        for line in file:
            print(line, end='')

    with open('journal.txt', 'a') as file:
        while True:
            entry = input("Add more journal entries (or type 'exit' to finish): ")
            if entry.lower() == 'exit': 
                break       
            timestamp = datetime.now().strftime("[%Y-%m-%D %H:%M:%S]")
            file.write(f"{timestamp} {entry}\n")
            print("New entry logged!")
    try: 
        with open('journal.txt', 'r') as file:
            entries_count = 0
            words_count = 0 
            for line in file:
                if line.strip():
                    entries_count += 1
                    words_count += len(line.split()) -1
            print("\nCounting entries and words:")
            print(f"Total Entries: {entries_count}")
            print(f"Total words count: {words_count}")
    except FileNotFoundError:
        print("journal.txt not found.")

if __name__ == "__main__":
    log_entry()