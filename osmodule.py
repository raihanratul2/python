import os
print(os.getcwd())
filename ="os_module/test1/deep"
if not os.path.exists(filename):
    os.makedirs(filename)
file = "log.txt"
file2 = "os_module/logbook2.txt"
if os.path.exists(file):
    os.rename(file,file2)
else:
    os.rename(file2,file)

def rename_file(**kwargs):
    if os.path.exists(kwargs["old"]):
        os.rename(kwargs["old"],kwargs["new"])
    else:
        print(f"{kwargs['old']} does not exist")

rename_file(old="os_module/logbook.txt",new="os_module/logbook2.txt")