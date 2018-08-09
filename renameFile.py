#!/user/bin/python  
#!conding=utf8  
  
import os
import sys

  
def renameDir(dirpath,ext = "lua"):
    g = os.walk(dirpath)  
    for path,d,filelist in g:  
        #print d;  
        for filename in filelist:  
            print os.path.join(path, filename) 
            filename.split('.')[-1]
            (name,extension) = os.path.splitext(filename)
            os.rename(os.path.join(path,filename),os.path.join(path,name+"."+ext))
if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print ("renameFile.py dirpath ext")
        sys.exit()
    dirpath = sys.argv[1]
    ext = "lua"
    if(len(sys.argv) > 2):
        ext = sys.argv[2]
    renameDir(dirpath,ext)  