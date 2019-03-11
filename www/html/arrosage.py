#!/usr/bin/env python3
import os
if os.path.exists("./arrosage.cam"):
        os.remove("./arrosage.cam")
        if os.path.exists("../arrosage.cam"):
           os.remove("../arrosage.cam")
        if os.path.exists("../html2/arrosage.cam"):
           os.remove("../html2/arrosage.cam")


else:
        fichier1=open("./arrosage.cam","w")
        fichier=open("../arrosage.cam","w")
        fichier2=open("../html2/arrosage.cam","w")
        fichier1.close()
        fichier2.close()
        fichier.close()
