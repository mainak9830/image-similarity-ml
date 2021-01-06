from flask import Flask,request,jsonify,render_template





#test link 1--- http://127.0.0.1:5000/?cloudpath_img1=my_image/fear.jpg&cloudpath_img2=my_image/me0.jpeg&emotion=0
#test link 2--- http://127.0.0.1:5000/?cloudpath_img1=my_image/me4.jpg&cloudpath_img2=my_image/me0.jpeg&emotion=3

app=Flask(__name__)



@app.route("/home")
def home():
    return render_template("index.html")

