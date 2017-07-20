#!/bin/bash
read -p "Enter message: " msg
sleep 2
echo "Starting..."
while :
do
    xdotool type "$msg"
    sleep 0.3
    xdotool key KP_Enter
    sleep 0.4
done
