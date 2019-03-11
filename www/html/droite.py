#!/usr/bin/env python3
import os
import time
if os.path.exists("./droite.cam") :
	os.remove("./droite.cam")
if os.path.exists("./gauche.cam") :
	os.remove("./gauche.cam")
time.sleep(0.2)
fichier=open("./droite.cam","w")
fichier.write("\n droite")
fichier.close()
