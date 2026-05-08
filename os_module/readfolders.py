import os
def read_folders(path):
    folders = []
    for item in os.listdir(path):
        item_path = os.path.join(path,item)
        if os.path.isdir(item_path):
            folders.append(item)
    return folders
def find_flac_files(path):
    flac_files = []
    for root, dirs, files in os.listdir(path):
        for file in files:
            if file.endswith('.flac'):
                flac_files.append(root,files)
    return flac_files


if __name__ == "__main__":
    path = input("Enter the path to read folders: ")
    folders = find_flac_files(path)
    print("Folders in the specified path:")
    for folder in folders:
        print(folder)
    print(folders)