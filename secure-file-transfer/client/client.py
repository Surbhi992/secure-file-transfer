import requests

SERVER_URL = "http://127.0.0.1:5000"

def upload_file(filepath):
    with open(filepath, "rb") as f:
        files = {"file": f}
        response = requests.post(f"{SERVER_URL}/upload", files=files)
        print(response.json())

def download_file(filename):
    response = requests.get(f"{SERVER_URL}/download/{filename}")

    with open(filename, "wb") as f:
        f.write(response.content)

    print("File downloaded:", filename)

if __name__ == "__main__":
    upload_file("test.txt")
    download_file("test.txt")
