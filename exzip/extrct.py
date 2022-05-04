import zipfile
import sys

args = sys.argv
filename = args[1]
path = "./result/"
passwd = args[2]
with zipfile.ZipFile(filename, "r") as zp:
    try:
        zp.extractall(path=path, pwd=passwd.encode("utf-8"))
        print("The extract is complete.")
    except RuntimeError as e:
        print(e)
