#!/usr/bin/env python3
import os
import time
if os.path.exists("./caldroite.cam") :
	os.remove("./caldroite.cam")
if os.path.exists("./calgauche.cam") :
	os.remove("./calgauche.cam")
time.sleep(0.2)
fichier=open("./caldroite.cam","w")
fichier.write("\n caldroite")
fichier.close()
