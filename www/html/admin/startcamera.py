#!/usr/bin/env python3
import os
import time
if os.path.exists("./startcamera.cam") :
	os.remove("./startcamera.cam")
time.sleep(0.2)

fichier=open("./startcamera.cam","w")
fichier.write("\n Start Camera")
fichier.close()
