#!/bin/sh

if [ -z $1 ]
then 
    echo "Usage: $0 { p | l | a }. p - portrait, l - landscape, a - auto"
elif [[ $1 == a* ]]
then 
    echo "Turning on automatic rotation"
    adb shell content insert --uri content://settings/system --bind name:s:accelerometer_rotation --bind value:i:1
else
    echo "Turning off automatic rotation"
    adb shell content insert --uri content://settings/system --bind name:s:accelerometer_rotation --bind value:i:0
    if [[ $1 == p* ]]
    then
        echo "Rotating screen portrait"
        adb shell content insert --uri content://settings/system --bind name:s:user_rotation --bind value:i:0
    elif [[ $1 == l* ]]
    then
        echo "Rotating screen landscape"
        adb shell content insert --uri content://settings/system --bind name:s:user_rotation --bind value:i:1
    fi
fi