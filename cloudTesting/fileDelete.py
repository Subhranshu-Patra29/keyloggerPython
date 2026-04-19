import firebase_admin
from firebase_admin import credentials, storage

def initialize_firebase():
    cred = credentials.Certificate('cloudTesting/credentials.json')
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'keylogger-e4335.appspot.com'
    })

def delete_files_in_folder(folder_path, bucket_name = 'keylogger-e4335.appspot.com'):
    # Initialize Firebase
    initialize_firebase()
    
    bucket = storage.bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=folder_path)
    
    for blob in blobs:
        blob.delete()
        print(f"Deleted: {blob.name}")

# # Specify your bucket name and folder path
# bucket_name = 'keylogger-e4335.appspot.com'
# folder_path = 'text/example.txt'

# # Delete all files in the folder
# delete_files_in_folder(folder_path)