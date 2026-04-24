# 🔐 Secure File Transfer & Encrypted Storage System

## 📌 Overview

This project is a secure file transfer system developed using Python. It enables safe file upload and download between a client and server by applying encryption techniques to ensure data confidentiality during transmission and storage.

---

## 🚀 Features

* 🔒 AES-based encryption and decryption
* 📤 Secure file upload to server
* 📥 Secure file download from server
* 🖥️ Client-server architecture using Flask
* 📁 Encrypted file storage on server
* ⚡ Lightweight and easy to run

---

## 🛠️ Technologies Used

* Python
* Flask
* PyCryptodome
* Requests

---

## 📂 Project Structure

secure-file-transfer/

├── server/
│   ├── server.py
│   ├── crypto_utils.py
│   └── requirements.txt

├── client/
│   ├── client.py

├── server_screenshot.png
├── client_screenshot.png

└── README.md

---

## ⚙️ How to Run the Project

### 🔹 Step 1: Start Server

cd server
pip install -r requirements.txt
python server.py

---

### 🔹 Step 2: Run Client

cd client
python client.py

---

## 🧪 Usage

1. Create a file named `test.txt` inside the client folder
2. Add any text inside the file
3. Run the client script
4. File will be uploaded to the server and downloaded back securely

---
## 📸 Output

### 🔹 Server Output
![Server Output](server_screenshot.png.png)


## 🔐 Security Concepts Implemented

* AES Encryption (ensures confidentiality)
* Secure file handling
* Client-server communication

---

## ⚠️ Limitations

* Uses AES ECB mode (not recommended for production)
* No authentication system
* Basic implementation for learning purposes

---

## 🔮 Future Enhancements

* Implement AES-CBC encryption mode
* Add HMAC for data integrity
* Introduce user authentication
* Develop web-based interface

---

## 👨‍💻 Author

Cyber Security Internship Project

---

## 📜 License

This project is for educational purposes only.

