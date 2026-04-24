# 🔐 Secure File Transfer & Encrypted Storage System

## 📌 Overview

This project implements a secure file transfer system that allows users to upload and download files between a client and server using encryption. The goal is to ensure data confidentiality during transmission and safe storage on the server.

---

## 🚀 Features

* AES-based file encryption and decryption
* Secure file upload and download
* Client-server architecture using Flask
* Encrypted file storage on server
* Lightweight and easy-to-run project

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

└── README.md

---

## ⚙️ How to Run

### 1. Start Server

cd server
pip install -r requirements.txt
python server.py

### 2. Run Client

cd client
python client.py

---

## 🧪 Usage

1. Create a file named `test.txt` inside the client folder
2. Add any text inside the file
3. Run the client script
4. File will be uploaded to server and downloaded back securely

---

## 🔐 Security Concepts

* AES Encryption
* Secure file handling
* Client-server communication

---

## ⚠️ Limitations

* Uses AES ECB mode (not recommended for production)
* No authentication system
* Basic implementation for learning purposes

---

## 🔮 Future Improvements

* AES-CBC encryption
* HMAC for integrity checking
* User authentication
* Web-based interface

---

## 👨‍💻 Author

Cyber Security Internship Project

---

## 📜 License

For educational purposes only.
