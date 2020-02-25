#!/usr/bin/env bash

if [ ! -z "$1" ]
then
    if [ "$1" = 'i' ]
    then
        # java maxconnect4 interactive [input_file] [computer-next/human-next] [depth]
        echo -e " \e[32mRunning interactive player-next \e[39m"

        python3 ./maxConnect4.py interactive inputs/input1.txt computer-next 10
        echo -e "\e[32mRunning interactive computer-next \e[39m"
        python3 ./maxConnect4.py interactive inputs/input1.txt player-next 10
    fi
    if [ "$1" = 'o' ]
    then
        # java maxconnect4 one-move [input_file] [output_file] [depth]
        echo -e " \e[32mRunning one-move input1 \e[39m"
        python3 ./maxConnect4.py one-move inputs/input1.txt output1.txt 10
        echo -e " \e[32mRunning one-move input2 \e[39m"
        python3 ./maxConnect4.py one-move inputs/input2.txt output2.txt 10
    fi
else
    echo -e "\e[31m No mode specified, exiting...\e[39m"
fi