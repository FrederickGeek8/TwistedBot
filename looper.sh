#!/bin/bash

players="$1"

usage() {
    echo ''
    echo "Usage: `basename $0` <players>"
    echo ' `players` -- number of player bots spawned'
    echo ''
    exit 1;
}

if [ -z "$players" ]; then
usage
fi

echo "WARNING: You must run 'killall -9 Python' to stop this script!"
sleep 2
echo ""
for i in `seq 1 $players`
do
python bot.py&
done
