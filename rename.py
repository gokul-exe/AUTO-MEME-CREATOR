import os

def rename_files():
    folder_path = "memes"
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    total_files = len(files)

    if total_files == 0:
        print("No files found in the folder.")
        return

    for idx, filename in enumerate(files, start=1):
        file_extension = os.path.splitext(filename)[1]
        new_filename = f"{idx}{file_extension}"
        src_path = os.path.join(folder_path, filename)
        dest_path = os.path.join(folder_path, new_filename)
        
        os.rename(src_path, dest_path)
        print(f"Renamed {filename} to {new_filename}")
    print("File renaming completed!")
if __name__ == "__main__":
    pass
    
    
    
