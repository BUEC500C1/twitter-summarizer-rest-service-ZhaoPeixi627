import sys
from flask import Flask, render_template, request, send_file
import os
import zipfile

application = Flask(__name__)

@application.route('/') 
def root():
    return render_template('my-form.html')

@application.route('/', methods=['POST']) 

def post():
    text1 = request.form['username'] 
    args = "python video.py"+" "+str(text1)
    os.system(args)    
    return send_file(str(text1)+'.avi', attachment_filename = str(text1)+'.avi', as_attachment=True)
    

if __name__ == '__main__':
#     app.run(debug=True)
    app.run(host="0.0.0.0", port=80)


