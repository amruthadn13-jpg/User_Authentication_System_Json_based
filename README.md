# User_Authentication_System_Json_based
# 🐍 Python Project – Day 31

## 🔐 User Authentication System (JSON-Based)

---

## 📌 Overview

This project is an upgraded version of the User Authentication System using **JSON for data storage** instead of a text file.

It allows users to:

* Register new accounts
* Login securely

All user data is stored in a structured JSON file (`users.json`), making it easier to manage and extend.

---

## 🚀 Features

✔ User Registration
✔ User Login
✔ JSON-Based Data Storage
✔ Prevent Duplicate Usernames
✔ Clean & Structured Data
✔ Error Handling

---

## 🧠 Concepts Used

* JSON Handling (`json.load`, `json.dump`)
* Lists & Dictionaries
* Functions
* Loops (`while`)
* Conditional Statements (`if-else`)
* Exception Handling (`try-except`)

---

## 📂 File Structure

```id="x0r6jq"
project_folder/
│
├── json_user_system.py
├── users.json
```

---

## 📄 Data Format (users.json)

User data is stored as a **list of dictionaries**:

```json id="9y9o36"
[
    {
        "username": "Amrutha",
        "password": "Amrutha@18"
    },
    {
        "username": "Padma",
        "password": "Padma@87"
    }
]
```

---

## ⚙️ How It Works

---

### 🔹 1. Register

* Takes username and password
* Checks for duplicate username
* Adds user as a dictionary
* Saves data in JSON file

---

### 🔹 2. Login

* Reads data from JSON file
* Compares username and password
* Displays success or failure message

---

## 🔄 Functions Explained

### 📥 `load_users()`

* Reads JSON file
* Converts JSON → Python list

---

### 📤 `save_users(users)`

* Writes Python list → JSON file
* Uses `indent` for better readability

---

### 🆕 `register()`

* Adds new user to list
* Prevents duplicate entries

---

### 🔐 `login()`

* Validates user credentials

---

## ❗ Error Handling

* Handles missing file (returns empty list)
* Prevents program crash
* Ensures valid data processing

---

## 💡 Example Output

```id="ppwsl2"
1. Register
2. Login
3. Exit

Enter choice: 1
Enter username: Amrutha
Enter password: 123

User registered successfully!
```

---

## 🎯 Key Learning

| Concept         | Description             |
| --------------- | ----------------------- |
| JSON            | Structured data storage |
| Dictionary      | Key-value data handling |
| List            | Store multiple users    |
| Data Conversion | JSON ↔ Python           |

---

## 🔥 Why JSON is Better than Text File

| Text File       | JSON              |
| --------------- | ----------------- |
| Needs splitting | Direct access     |
| Error-prone     | Safe & structured |
| Hard to scale   | Easy to extend    |

---

## 🔮 Future Improvements

* Add Change Password feature
* Add Delete User feature
* Encrypt passwords (security)
* Use database (SQLite/MySQL)
* Build web version (Flask/Django)

---

## 🙌 Conclusion

This project demonstrates how to use **JSON for structured data storage** and builds a strong foundation for:

* Web development
* API handling
* Real-world applications

---

**Author**
Amrutha D N

⭐ A step closer to becoming a full-stack developer!
