#!/usr/bin/env python3
import os
if os.path.exists("./lumiere.cam") :
    os.remove("./lumiere.cam")
    if os.path.exists("/home/pi/www/html2/lumiere.cam"):
        os.remove("/home/pi/www/html2/lumiere.cam")


else:
    
    fichier=open("./lumiere.cam","w")
    fichier1=open("/home/pi/www/html2/lumiere.cam","w")
    fichier1.close()
    fichier.close()
