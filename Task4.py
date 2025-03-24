def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."
    return inner

contacts = {}

@input_error
def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args):
    name = args[0]
    return contacts[name]

@input_error
def show_all(args):
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    while True:
        command = input("Enter a command: ").strip().lower()
        if command == "exit":
            break
        elif command == "add":
            args = input("Enter the argument for the command: ").strip().split()
            print(add_contact(args))
        elif command == "phone":
            args = input("Enter the argument for the command: ").strip().split()
            print(get_phone(args))
        elif command == "all":
            print(show_all([]))
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()