from flask import Flask, request, jsonify 

#from database import *
import os
import json

#init app 
app = Flask(__name__)

@app.route('/')
def serve(id):
    service = {'name' : 'thanuja'}
    json_object = json.dumps(service, indent = 4) 
    print(json_object)
    return json_object

if __name__ == "__main__" : 
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
