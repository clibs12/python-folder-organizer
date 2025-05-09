import os
import shutil
import tkinter as tk
from tkinter import filedialog

def organize_files(path):
    # Get all files in the directory (ignore directories)
    file_names = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    
    # Process each file
    for file_name in file_names:
        # Split filename and extension
        name, ext = os.path.splitext(file_name)
        ext = ext.lower()  # make extension lowercase for consistency
        
        # Skip files without extensions
        if not ext:
            continue
        
        # Create folder name from extension (remove the dot and capitalize)
        folder_name = f"{ext[1:].upper()} Files"
        
        # Create folder if it doesn't exist
        folder_path = os.path.join(path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Move the file
        src_path = os.path.join(path, file_name)
        dest_path = os.path.join(folder_path, file_name)
        
        # Only move if file doesn't already exist in destination
        if not os.path.exists(dest_path):
            try:
                shutil.move(src_path, dest_path)
                print(f"Moved: {file_name} → {folder_name}/")
            except Exception as e:
                print(f"Error moving {file_name}: {e}")



root = tk.Tk()
root.withdraw()
path = filedialog.askdirectory(title="Select a folder to organize")
if path:
    organize_files(path)
else:
    print("No folder selected.")    
