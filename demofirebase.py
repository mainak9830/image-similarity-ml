#import library
import pyrebase

#config file
config={
    'apiKey': "AIzaSyBEQ4hSxSQWULvKNaguUgSN5xCqp-2VP9I",
    'authDomain': "demoapp-a9491.firebaseapp.com",
    'databaseURL': "https://demoapp-a9491-default-rtdb.firebaseio.com",
    'projectId': "demoapp-a9491",
    'storageBucket': "demoapp-a9491.appspot.com",
    'messagingSenderId': "877663279152",
    'appId': "1:877663279152:web:202f42d98be700f33b75f5",
    'measurementId': "G-00JSBFE6MX"
}

#initialize the app
firebase=pyrebase.initialize_app(config)

#Invoke the storage of Firebase
storage=firebase.storage()
