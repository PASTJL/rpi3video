import os
import time
import sys
import stat
import RPi.GPIO as GPIO
import subprocess


def eraseFiles(repertoire):

  files=os.listdir(repertoire)
  for i in range(0,len(files)):
   os.remove(repertoire+'/'+files[i])


def step_4 (p):

    if p==0:
            GPIO.output(17,0)
            GPIO.output(22,0)
            GPIO.output(23,0)
            GPIO.output(24,0)

    if p==1:
            GPIO.output(17,1)
            GPIO.output(22,1)
            GPIO.output(23,0)
            GPIO.output(24,0)

    if p==2:
            GPIO.output(17,0)
            GPIO.output(22,1)
            GPIO.output(23,1)
            GPIO.output(24,0)
    if p==3:
            GPIO.output(17,0)
            GPIO.output(22,0)
            GPIO.output(23,1)
            GPIO.output(24,1)
    if p==4:
            GPIO.output(17,1)
            GPIO.output(22,0)
            GPIO.output(23,0)
            GPIO.output(24,1)
            


def steps_4(value):
    print (value)
    global pas
    if(value<0):
        for i in range (0,abs(value)):
            step_4(pas)
            time.sleep(0.005)
            pas+=1
            if(pas>=5):
               pas=1;

    else:
        for i in range (0,abs(value)):
            step_4(pas)
            time.sleep(0.005)
            if(pas==1):
               pas=5;
            pas-=1
    step_4(0)

def steps_10Deg(nb10deg):
    steps_4(51*nb10deg) 


def mvCamera(st) :
      global counter
      if counter+st > 12:
        steps_10Deg(12-counter)
        counter=12
        fichier = open("/home/pi/www/html/counter.cam", "w")
        fichier.write("12")
        fichier.close()
      if counter+st <0 :
        steps_10Deg(-counter)
        counter=0
        fichier = open("/home/pi/www/html/counter.cam", "w")
        fichier.write("0")
        fichier.close()
      if counter+st >=0 and counter+st <=12 :
        print("4 phase moving")
        steps_10Deg(st)
        counter+=st
        fichier = open("/home/pi/www/html/counter.cam", "w")
        fichier.write(str(counter))
        fichier.close()
      print("counter=",counter)


if __name__ == "__main__":
     counter=0
     if os.path.exists("/home/pi/www/html/counter.cam"):
        fichier = open("/home/pi/www/html/counter.cam", "r")
        counter=int(fichier.readline().rstrip('\n\r'))
        fichier.close()
     else:
        fichier = open("/home/pi/www/html/counter.cam", "w")
        fichier.write("0")
        fichier.close()


     GPIO.setmode(GPIO.BCM)
     GPIO.setwarnings(False)
     GPIO.setup(17, GPIO.OUT)
     GPIO.setup(22, GPIO.OUT)
     GPIO.setup(23, GPIO.OUT)
     GPIO.setup(24, GPIO.OUT)

     GPIO.setwarnings(False)
# defini le port GPIO 4 comme etant une sortie output
     GPIO.setup(4, GPIO.OUT)
     GPIO.output(4,GPIO.HIGH)
     GPIO.setup(20, GPIO.OUT)
     GPIO.output(20,GPIO.HIGH)
     step_4(0)
     pas=1
# detection fichier gauche.cam droite.cam calgauche.cam caldroite.cam
     while True :
       if os.path.exists("/home/pi/www/html/droite.cam"):
         os.remove("/home/pi/www/html/droite.cam")
         mvCamera(1)
       if os.path.exists("/home/pi/www/html/gauche.cam"):
         os.remove("/home/pi/www/html/gauche.cam")
         mvCamera(-1)
       if os.path.exists("/home/pi/www/html/calgauche.cam"):
         os.remove("/home/pi/www/html/calgauche.cam")
         counter=0
         fichier = open("/home/pi/www/html/counter.cam", "a")
         fichier.write("0")
         fichier.close()
       if os.path.exists("/home/pi/www/html/caldroite.cam"):
         os.remove("/home/pi/www/html/caldroite.cam")
         counter=12
         fichier = open("/home/pi/www/html/counter.cam", "a")
         fichier.write("12")
         fichier.close()
       # ne pas eclairer ou arroser plus de une heure
       if os.path.exists("/home/pi/www/html/lumiere.cam"):
            GPIO.output(4,GPIO.LOW)
            if (time.time() - os.stat("/home/pi/www/html/lumiere.cam")[stat.ST_MTIME] > 3600 ) :
                 os.remove("/home/pi/www/html/lumiere.cam")
                 if os.path.exists("/home/pi/www/html2/lumiere.cam"):
                     os.remove("/home/pi/www/html2/lumiere.cam")
       else :
            GPIO.output(4,GPIO.HIGH)

       if os.path.exists("/home/pi/www/html/arrosage.cam"):
            GPIO.output(20,GPIO.LOW)
            if (time.time() - os.stat("/home/pi/www/html/arrosage.cam")[stat.ST_MTIME] > 3600 ) :
                 os.remove("/home/pi/www/html/arrosage.cam")
                 if os.path.exists("/home/pi/www/html2/arrosage.cam"):
                    os.remove("/home/pi/www/html2/arrosage.cam")
                 if os.path.exists("/home/pi/www/arrosage.cam"):
                    os.remove("/home/pi/www/arrosage.cam")
       else :
            GPIO.output(20,GPIO.HIGH)       
 

       if os.path.exists("/home/pi/www/html/admin/delmovies.cam"):
         os.remove("/home/pi/www/html/admin/delmovies.cam")
         eraseFiles("/home/pi/www/html/motion")
         time.sleep(1)
         cmde="sudo systemctl restart dropbox"
         try :
            p = subprocess.Popen(cmde,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            p.wait()
             # (output, err) = p.communicate()
         except :
            pass


       if os.path.exists("/home/pi/www/html/admin/startcamera.cam"):
         os.remove("/home/pi/www/html/admin/startcamera.cam")
         os.system("sudo /etc/motion/motionstart.sh")
       if os.path.exists("/home/pi/www/html/admin/stopcamera.cam"):
         os.remove("/home/pi/www/html/admin/stopcamera.cam")
         os.system("sudo /etc/motion/motionstop.sh")
    


       time.sleep(0.5)
