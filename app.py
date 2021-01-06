from flask import Flask,request,jsonify,render_template

from demofirebase import *   #import the firebase config file
#from deepface import DeepFace
import matplotlib.pyplot as plt

#test link 1--- http://127.0.0.1:5000/?cloudpath_img1=my_image/fear.jpg&cloudpath_img2=my_image/me0.jpeg&emotion=0
#test link 2--- http://127.0.0.1:5000/?cloudpath_img1=my_image/me4.jpg&cloudpath_img2=my_image/me0.jpeg&emotion=3

app=Flask(__name__)

emotions={'0' : 'angry','1' : 'disgust','2' : 'fear','3' : 'happy','4' : 'sad','5' : 'surprise','6' : 'neutral'}
@app.route('/',methods=['GET'])
def hello_world():
    
    result={}
    emotion=str(request.args['emotion'])
    #cloud and local path for image1  ----------------------------->Camera Image Uploaded 
    path_on_cloud_img1=str(request.args['cloudpath_img1'])
    path_on_local_img1="firebase_image/firebase1.jpg"

    #cloud and local path for image2  ------------------------------>Verified Image 
    path_on_cloud_img2=str(request.args['cloudpath_img2'])
    path_on_local_img2="firebase_image/firebase2.jpg"

    #download the first image from cloud to local storage
    storage.child(path_on_cloud_img1).download(path_on_local_img1)

    #download the second image from cloud to local storage
    storage.child(path_on_cloud_img2).download(path_on_local_img2)

    #verify the two images are similar or not
    #result  = DeepFace.verify(path_on_local_img1,path_on_local_img2)
    
    result["verified"]=False
    result["emotion_verify"]=False

    #if(result["verified"]!=True):
     #   return result

    img=plt.imread('firebase_image/firebase1.jpg')

    #pred=DeepFace.analyze(img,actions=['emotion'])


    #if(pred['dominant_emotion'] == emotions[emotion]):
     #   result["emotion_verify"]=True
    
    result['img']=img
    return result

@app.route("/home")
def home():
    return render_template("index.html")

