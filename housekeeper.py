import os
import shutil

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

folders = {
    "Documents": [".pdf", ".docx", ".xlsx"],
    "Photos": [".jpg", ".jpeg", ".png", ".gif"],
    "Video": [".mp4", ".avi", ".mkv"],
    "Misc": []
}

def organize_and_move():
    for file in os.listdir(downloads_path):
        file_path = os.path.join(downloads_path, file)
        
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            moved = False

            for folder, extensions in folders.items():
                if file_ext in extensions:
                    folder_path = os.path.join(downloads_path, folder)
                    
                    # Create folder if it doesn't exist
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    
                    print(f"Moving '{file}' to '{folder_path}'...")
                    shutil.move(file_path, os.path.join(folder_path, file))
                    moved = True
                    break

            # Move to 'Misc' if no matching folder
            if not moved:
                print(f"Moving '{file}' to Misc folder...")
                folder_path = os.path.join(downloads_path, "Others")
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                shutil.move(file_path, os.path.join(folder_path, file))

def auto_arrange():
    pass

organize_and_move()