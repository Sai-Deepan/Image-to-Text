#Sai

from flask import Flask, request, render_template
import cv2
import numpy as np
import Reader

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    in_memory_file = file.read()
    npimg = np.frombuffer(in_memory_file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    text = Reader.extract_text_from_image_cv2(img)

    Reader.write_text_to_file(text, "./output.txt")

    return f"<h2>Extracted Text:</h2><pre>{text}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
