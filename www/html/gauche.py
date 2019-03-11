#!/usr/bin/env python3
import os
import time
if os.path.exists("./gauche.cam") :
	os.remove("./gauche.cam")
if os.path.exists("./droite.cam") :
	os.remove("./droite.cam")
time.sleep(0.2)

fichier=open("./gauche.cam","w")
fichier.write("\n gauche")
fichier.close()
