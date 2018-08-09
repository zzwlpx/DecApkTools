#!/user/bin/python  
#!conding=utf8 
import zlib
import sys
import os

def compressStr(msg):
    compressed = zlib.compress(msg)
    return compressed
    
def decompressStr(commsg):
    decompressed = zlib.decompress(commsg)
    return decompressed
    
def compress(infile, dst, level=9):
    infile = open(infile, 'rb')
    dst = open(dst, 'wb')
    compress = zlib.compressobj(level)
    data = infile.read(1024)
    while data:
        dst.write(compress.compress(data))
        data = infile.read(1024)
    dst.write(compress.flush())

def decompress(infile, dst):
    infile = open(infile, 'rb')
    dst = open(dst, 'wb')
    decompress = zlib.decompressobj()
    data = infile.read(1024)
    while data:
        dst.write(decompress.decompress(data))
        data = infile.read(1024)
    dst.write(decompress.flush())
def decompressDir(dirpath):
    dirpath=dirpath.strip()
    dirpath=dirpath.rstrip("\\")
    newDir = dirpath + "plain"
    ##parentDir = os.path.abspath(os.path.join(dirpath, ".."))
    g = os.walk(dirpath)  
    for path,d,filelist in g:  
        #print d;  
        for filename in filelist:  
            filepath =  os.path.join(path, filename) 
            print filepath
            distPath = filepath.replace(dirpath,newDir)
            fileDir , tmpName = os.path.split(distPath)
            isExists=os.path.exists(fileDir)
            if not isExists:
                os.makedirs(fileDir) 
            decompress(filepath, distPath)
            print distPath + "succeed!"
if __name__ == "__main__":
    #compress('in.txt', 'out.txt')
    if(len(sys.argv) < 2):
        print sys.argv[0] + " filePath / destPath"
        sys.exit()
    if(os.path.isfile(sys.argv[1])):
        decompress(sys.argv[1], sys.argv[2])
        sys.exit()
    if(os.path.isdir(sys.argv[1])):
        decompressDir(sys.argv[1])
        sys.exit()
    print ( " path is error! " )
    