#!/bin/bash
ping -c 1 192.168.1.1
if [ $? -ne 0 ]; then
	sudo ifconfig wlan0
	sleep 1
	ping -c 1 192.168.1.1
        if [ $? -ne 0 ]; then
            sudo ifconfig wlan0
            sleep 1
	    ping -c 1 192.168.1.1
            if [ $? -ne 0 ]; then
		sudo reboot
            fi
	fi
fi
