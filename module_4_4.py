def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    value = contacts.get(name)
    if value == None:
        contacts[name] = phone
        return "Contact added."
    else:
        return "Contact is out."

def change_phone(args, contacts):
    name, phone = args
    value = contacts.get(name)
    if value != None:
        contacts[name] = phone
        return "change phone."
    else:
        return "contact is not lost"
    

def phone_print(args, contacts):
    name = args[0]
    value = contacts.get(name)
    if value != None:
        return contacts[name]
    else:
        return "contact is not lost" 

def all_print(contacts):
    for key, value in contacts.items():
        print(f"{key} {value}")    

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_phone(args, contacts))
        elif command == "phone":
            print(phone_print(args, contacts))
        elif command == "all":
            all_print(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()