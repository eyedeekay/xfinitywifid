#!/bin/bash

pkill "kill_captive_network_assistant"
./kill_captive_network_assistant.sh &

while true
do
	ping -i 1 -c 2 'www.google.com' > /dev/null 2>&1
	if [ $? -eq 0 ]; then
		printf 'connection good :) '
		pkill 'firefox'
		sleep 3
	else
		printf 'connection fail :( '
		./xfinity.py
		sleep 1
	fi
done
