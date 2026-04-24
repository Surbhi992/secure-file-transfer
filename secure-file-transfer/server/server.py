from flask import Flask, request, jsonify, send_file
import os
from crypto_utils import decrypt_file, encrypt_file

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    decrypt_file(filepath)
    return jsonify({"message": "File uploaded & decrypted successfully"})

@app.route("/download/<filename>", methods=["GET"])
def download(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    encrypt_file(filepath)
    return send_file(filepath, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
