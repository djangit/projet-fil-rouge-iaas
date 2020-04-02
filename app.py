import os, pprint, filetype, base64, json
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import csv
import boto3, logging
from botocore.exceptions import ClientError
#from flask_oauth import OAuth

UPLOAD_FOLDER = '/home/lpirbay/Documents/pfr'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv'}
s3 = boto3.client('s3')
#s3 = boto3.resource('s3')
#bucket = s3.Bucket('bucket-projet-fil-rouge')

app = Flask(__name__)

#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/toto', methods=['POST'])
def upload_file():
    
    output={}
    # check if the post request has the file part
    if 'file' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        return resp, 400

    file = request.files['file']

    if file.filename == '':
        resp = jsonify({'message' : 'No file selected for uploading'})
     
        return resp, 400

    if file and allowed_file(file.filename):
        file_name= file.filename
        file_name = file_name.split(".")

        if 'text' in file.content_type or 'application/octet-stream' in file.content_type:
            fileMetadata = {}
            file_tmp = request.files['file'].read()
            file_tmp = file_tmp.decode("utf8")
            #metadata_txt['file name']=file_name[0]
            fileMetadata['name']=file.filename
            fileMetadata['size']=len(file.tmp)
            fileMetadata['type']=file.content_type            
            output['File Data']= file_tmp
            output['File MetaData'] = fileMetadata
            '''try:
               response = s3_client.upload_file(file_name, bucket, object_name)
               response = s3.upload_file(file. 
            except ClientError as e:
               logging.error(e)
               return False
            return True
            '''
            return jsonify(output),200

        elif 'image' in file.content_type: 
            fileMetadata={}
            encoded_string = base64.b64encode(file.read())
            encoded_string = encoded_string.decode('utf-8')
            fileMetadata['name']=file.filename
            fileMetadata['size']=len(encoded_string)
            fileMetadata['type']=file.content_type  
            output['File data']=encoded_string
            output['File Metadata']=fileMetadata
            return jsonify(output),200


    else:
        resp = jsonify({'File not supported' : 'please upload a csv, png or txt file'})
        return resp, 400

    
