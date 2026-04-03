import json

FILE_NAME = "users.json"


def load_users():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_users(users):
    with open(FILE_NAME, "w") as file:
        json.dump(users, file, indent=4)


def register():
    users = load_users()

    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:
        if user["username"] == username:
            print("Username already exists!")
            return

    users.append({"username": username, "password": password})
    save_users(users)

    print("User registered successfully!")


def login():
    users = load_users()

    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:
        if user["username"] == username and user["password"] == password:
            print("Login successful!")
            return

    print("Invalid credentials!")


# Menu
while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        break

    else:
        print("Invalid choice!")
