#!/usr/bin/python3
import os
import time
import subprocess
if __name__ == "__main__" :
    
  while True :
    liste=os.listdir("/home/pi/motion") 
    for file in liste:
        age=0
       # st_mtime date in sec
        try :
           last_time= round(os.stat("/home/pi/motion/"+file).st_mtime )
           # time.time() current time in seconds
           age=round(time.time() -last_time)
        except :
          age=0
          pass
        if (os.path.exists("/home/pi/motion/"+file) and file.endswith("jpg")) :
           cmde="/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/motion/"+file+" /"
           try :
              p = subprocess.Popen(cmde,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
              p.wait()
             # (output, err) = p.communicate()
           except :
              pass
      
              if (age > 86400) :
                 os.remove("/home/pi/motion/"+file);
            
        if (os.path.exists("/home/pi/motion/"+file) and file.endswith("mkv")) :
           cmde="/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/motion/"+file+" /"
           if (age > 40 and os.stat("/home/pi/motion/"+file).st_size > 1024000) :
               try :
                  p = subprocess.Popen(cmde,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                  p.wait()
                #  (output, err) = p.communicate()
               except :
                 pass   
           if (age > 86400 or (age >40 and os.stat("/home/pi/motion/"+file).st_size < 1024000)) :
             try :
                os.remove("/home/pi/motion/"+file);
             except :
                 pass  
               
  time.sleep(10)
