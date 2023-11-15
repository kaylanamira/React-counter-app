from flask import Flask, jsonify, request, json
from werkzeug.utils import secure_filename 
import urllib.request
import os


app = Flask(__name__)

UPLOAD_FOLDER = '../images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def getData():
    return {
        'id': 4,
        'title': "Flask app",
        'name': "hi"
    }
@app.route('/upload', methods=['POST'])
def upload_image():
    #checks the existence of file
    if 'files[]' not in request.files:
        resp = jsonify({
            "message": 'File is not requested',
            "status": 'failed'
        })
        resp.status_code = 400
        return resp
    
    files = request.files.getlist('files[]')

    #iterate for the file in request files
    for file in files:      
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            destpath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(destpath)

            success = True
        else:
            resp = jsonify({
                "message": 'File type is not allowed',
                "status": 'failed'
            })
            return resp

    if success:
        resp = jsonify({
            "message": 'Files successfully uploaded',
            "status": 'successs'
        })
        resp.status_code = 201
        return resp
    return resp
if __name__ == '__main__':
    app.run(debug=True)