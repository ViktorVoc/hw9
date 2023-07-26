def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input format. Please enter name and phone separated by space."
        except IndexError:
            return "Invalid input format. Please enter name and phone separated by space."
    return wrapper

contacts = {}

@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact '{name}' with phone '{phone}' has been added."

@input_error
def change_contact(name, phone):
    contacts[name] = phone
    return f"Contact '{name}' phone number has been changed to '{phone}'."

@input_error
def phone_contact(name):
    return f"Phone number for '{name}': {contacts[name]}"

def show_all_contacts():
    if not contacts:
        return "No contacts found."
    output = "Contacts:\n"
    for name, phone in contacts.items():
        output += f"{name}: {phone}\n"
    return output

def main():
    print("How can I help you?")
    while True:
        command = input().strip().lower()

        if command == "good bye" or command == "close" or command == "exit":
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command.startswith("add "):
            _, name, phone = command.split(" ", 2)
            print(add_contact(name, phone))
        elif command.startswith("change "):
            _, name, phone = command.split(" ", 2)
            print(change_contact(name, phone))
        elif command.startswith("phone "):
            _, name = command.split(" ", 1)
            print(phone_contact(name))
        elif command == "show all":
            print(show_all_contacts())
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
