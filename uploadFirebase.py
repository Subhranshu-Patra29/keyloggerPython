import datetime

def uploadToFirebase(storage, path_on_system, filetype):
    
    # go to specific folder depending on file type
    if filetype == 1: # text file
        path_on_cloud = "text/"
    elif filetype == 2: # video file
        path_on_cloud = "videos/"
    else: 
        path_on_cloud = "misc/"
          
    # Check if '/' is present in the path
    if '/' in path_on_system:
        pos1 = path_on_system.rindex('/')
    else:
        pos1 = -1
    pos2 = path_on_system.rindex('.')  
    
    # Get the current date and time
    now = datetime.datetime.now()

    # Format the date and time to be used in the filename
    formatted_now = now.strftime("%Y-%m-%d_%H-%M-%S")

    # append the original filename 
    path_on_cloud = path_on_cloud + path_on_system[ pos1 + 1 : pos2] + formatted_now + path_on_system[pos2:] 

    # upload
    storage.child(path_on_cloud).put(path_on_system)