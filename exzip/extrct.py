import zipfile
import sys
import glob

filename = "".join(glob.glob('*.zip'))
path = "./result/"
passwd = sys.argv[1]
with zipfile.ZipFile(filename, "r") as zp:
    try:
        zp.extractall(path=path, pwd=passwd.encode("utf-8"))
        print("complete.")
    except RuntimeError as e:
        print(e)
