#!/bin/bash
sudo cp  /etc/motion/motion.conf.jour /etc/motion/motion.conf
sleep 1
/etc/motion/motionstart.sh
