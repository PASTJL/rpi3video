
#!/bin/bash
sudo killall motion >/dev/null 2>&1 
sudo rm -f /home/pi/motion.pid /home/pi/motion.log /home/pi/nohup.out >/dev/null 2>&1
(nohup sudo /usr/bin/motion  >/dev/null 2>&1) & 

