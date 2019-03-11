#!/usr/bin/env python3
import os
import time
if os.path.exists("./stopcamera.cam") :
	os.remove("./stopcamera.cam")
time.sleep(0.2)

fichier=open("./stopcamera.cam","w")
fichier.write("\n Stop Camera")
fichier.close()
