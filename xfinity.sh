#!/bin/bash

echo 'Will attempt to sustain free connection to xfinitywifi :)'
echo "Press ctrl-c to stop"; echo

while true
do
   printf 'checking connection to google.com... '
   ping -c 3 google.com > /dev/null 2>&1
   if [ $? -eq 0 ]; then
      printf 'connection successful.\n'
      sleep 10
   else
      printf 'connection failed. rerunning connection script.\n'
      ./xfinity.py
   fi
   sleep 1
done
