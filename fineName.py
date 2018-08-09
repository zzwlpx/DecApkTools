#!/user/bin/python  
#!conding=utf8  
  
import os
g = os.walk("G:\\project\\qipaiWinPcap\\srcxxtea")
  
  
for path,d,filelist in g:  
    #print d;  
    for filename in filelist:  
        print os.path.join(path, filename) 
        filename.split('.')[-1]
		(name,extension) = os.path.splitext(filename)
        os.rename(os.path.join(path,filename),os.path.join(path,name+'.lua'))       