import os 
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from predicao import predict

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(),'upload')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/upload", methods=['POST'])
def upload():
    file = request.files['imagem']
    savePath = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(savePath)
    resultado = predict()
    return render_template('predicao.html', resultado = resultado)


if __name__ == '__main__':
    app.run(debug=True)