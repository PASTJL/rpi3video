#!/bin/bash
sleep 120
sudo /etc/motion/motionstart.sh 
sleep 10
sudo /usr/sbin/apachectl restart
