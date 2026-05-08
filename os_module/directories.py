# import os
# import shutil
# print("enter:")
# pathread = []
# location= "E:\\alac"
# with os.scandir(str(location)) as entries:
#     for entry in entries:
#         if entry.is_file():
#             print("file:",entry.name)
#         elif entry.is_dir():
#             pathread.append(os.path.normpath(os.path.abspath(entry.path)))
#             # print("\n dir:",os.path.normpath(os.path.abspath(entry.path)))

# # for path in pathread:
# #     print("\n dir:",path)
# print(pathread)
# filepaths=[]
# def findfiles(path):
#     if os.path.exists(path):
#         with os.scandir(path) as entries:
#             for entry in entries:
#                 if entry.is_dir():
#                     findfiles(entry.path)
#                     print(f"in func folder found {entry.name}")
#                 elif entry.is_file():
#                     filepath = os.path.join(path, entry.name)
#                     filepaths.append(filepath)
#                     print(f"in func file found: {filepath}")
#                 elif entry.is_file() or entry.is_dir():
#                     return f"in func nothing found, |{entry.name}| is not a file or folder"
#     else:
#         return "in func path does not exist"
# for path in pathread:
#     finding = findfiles(path)

# for file in filepaths:
#     newfile = os.path.join("E:\\newfolder", os.path.basename(file))
    
#     shutil.move(file, newfile)
#     print(f"moved {file} to {newfile}")


from pathlib import Path
import shutil

source = Path(r"E:\alac")
dest = Path(r"E:\newfolder")
dest.mkdir(parents=True, exist_ok=True)

for file in source.rglob("*"):
    if file.is_file():
        shutil.move(str(file), str(dest / file.name))
        print(f"Moved: {file.name}")