from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
import colordescriptor
import searcher
import cv2
import urllib.request as urllib2
import csv
from skimage import io
app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")

@app.route('/uploader', methods = ['POST'])
def upload_file():
    
    if request.method == 'POST':
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'static','uploads', secure_filename(f.filename))
#file path is an input image
        #frame=cv2.imread(file_path)
        frame=io.imread(file_path)
        print(file_path)
        #cv2.imshow('Input',frame)
        f.save(file_path)
        cd = colordescriptor.ColorDescriptor((8, 12, 3))
        query = frame
        features = cd.describe(query)
        search = searcher.init('index.csv')
        results = searcher.search(queryFeatures=features,indexPath='index.csv',limit=10)
        results=results[0:1]
        print(results)

        if results[0][1]=='dataset\\1.jpg':
            preds='pupa'
        elif  results[0][1]=='dataset\\2.jpg':
            preds='Cnaphalocrocis Medinalis'
        elif  results[0][1]=='dataset\\3.jpg':
            preds='Caterpillar'
        elif  results[0][1]=='dataset\\4.jpg':
            preds='Cnaphalocrocis Medinalis'
        elif  results[0][1]=='dataset\\5.jpg':
            preds='Cnaphalocrocis Medinalis'
        elif  results[0][1]=='dataset\\6.jpg':
            preds='Cnaphalocrocis Medinalis'
        elif  results[0][1]=='dataset\\7.jpg':
            preds='Cnaphalocrocis Medinalis'
        elif  results[0][1]=='dataset\\8.jpg':
            preds='Caterpillar'
        elif  results[0][1]=='dataset\\9.jpg':
            preds='Cnaphalocrocis Medinalis'
        elif  results[0][1]=='dataset\\10.jpg':
            preds='Cnaphalocrocis Medinalis'
        elif  results[0][1]=='dataset\\11.jpg':
            preds='Cnaphalocrocis Medinalis'
        elif  results[0][1]=='dataset\\12.jpg':
            preds='Diatraea Saccharalis'
        elif  results[0][1]=='dataset\\13.jpg':
            preds='Diloboderus Abderus'
        elif  results[0][1]=='dataset\\14.jpg':
            preds='Diatraea Saccharalis'
        elif  results[0][1]=='dataset\\15.jpg':
            preds='Neocurtilla Hexadactyla'
        elif  results[0][1]=='dataset\\16.jpg':
            preds='Neocurtilla Hexadactyla'
        elif  results[0][1]=='dataset\\17.jpg':
            preds='Neocurtilla Hexadactyla'
        elif  results[0][1]=='dataset\\18.jpg':
            preds='Leptotrombidium'
        elif  results[0][1]=='dataset\\19.jpg':
            preds='Leptotrombidium'
        elif  results[0][1]=='dataset\\20.jpg':
            preds='Leptotrombidium'
        elif  results[0][1]=='dataset\\21.jpg':
            preds='Leptotrombidium'
        else:
             preds='Invalid Insect'
            
           
        
    return render_template("upload.html",predictions=preds,display_image=f.filename)

if __name__ == "__main__":
    app.run()
    #cv2.imshow('Input',frame)
