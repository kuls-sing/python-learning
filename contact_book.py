import os

contacts = []
FILENAME = "contacts.txt"
def load_contacts():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            for line in f:
                try:
                    parts = line.strip().split(",")
                    contacts.append({"name": parts[0], "phone": parts[1], "email": parts[2]})
                except IndexError:
                    print(f"Skipping bad line: {line.strip()}")

def save_contacts():
    with open(FILENAME, "w") as f:
        for contact in contacts:
            f.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")

def show_menu():
    print("\n--- Contact Book ---")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Quit")
    
def add_contact():
    name = input("Enter name: ")
    if name == "":
        print("Name cannot be empty!")
        return
    phone = input("Enter phone number: ")
    if phone == "":
        print("Phone cannot be empty!")
        return
    email = input("Enter email: ")
    if email == "":
        print("Email cannot be empty!")
        return
    contacts.append({"name":name, "phone": phone, "email": email})
    print(f"Contact {name} is added!")

def view_contacts():
    if len(contacts) == 0:
        print("No contacts yet.")
    else:
        print("\n--- All Contacts ---")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")

def search_contact():
    query = input("Enter teh name to serach: ").lower()
    flag = False
    for contact in contacts:
        if query in contact["name"].lower():
            print(f"Found: {contact['name']} | {contact['phone']} | {contact['email']}")
            flag = True
    if not flag:
        print("No contact found.")

def main():
    load_contacts()
    try:
        while True:
            show_menu()
            choice = input("Choose an option (1-4): ")
            if choice == "1":
                add_contact()
            elif choice == "2":
                view_contacts()
            elif choice == "3":
                search_contact()
            elif choice == "4":
                save_contacts()
                print("Goodbye!")
                break
            else:
                print("Invalid option, try again.")
    except KeyboardInterrupt:
          print("\nForce quit detected. Saving contacts...")
          save_contacts() 

main()