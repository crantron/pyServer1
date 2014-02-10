#-------------------------------------#
#-Chris Anderson
#-CPSC Unix and Open Source Programming
#-May 11, 2011
#-------------------------------------#
import socket
import string
 
host = ''
port = 8000
counter = 0
fcounter = 0
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind((host,port))
sock.listen(1)
 
#---------------------------------------#
#-PrintToFile---------------------------#
#-param 1:Takes a string of the file name of
#-file to be opened.
#-param 2: the object of the file to be
#-writen to.
#---------------------------------------#
def PrintToFile( fname , fobj) :
    try:
        f = open(fname, 'r')
               fobj.write(f.read())
        f.close()
        return 1 #FOO! it works
        except IOError:
          f = open("404.html", 'r')
          fobj.write(f.read())
          f.close()
          return 0 #BAR...it doesn't
        
 
 
while 1:
    csock,caddr = sock.accept()
    cfile = csock.makefile('rw',0)
    line = cfile.readline().strip()
    lineArray = string.split(line) #make an array of the requestion line        
     request = lineArray[0] # Either will have 'GET' or 'Post'
    cmd = lineArray[1] # will have file name WITH / infront
     filename = cmd[1:] #cmd[ skip to 1 pos , then interpet rest ]
 
 
    if (request != "GET") :
        print('400 : Bad Request Type')
        PrintToFile("400.html", cfile)
    else :
        if cmd[0] == "/" :
 
            if filename == "STATUS" :
                cfile.write('<html><head><title>We are Up and Running!!!</title></head><body>')
                cfile.write(' The server has served : %s pages this session' %(counter))
                cfile.write(' The server has not found : %s pages this session' %(fcounter))
                cfile.write('</body>')
