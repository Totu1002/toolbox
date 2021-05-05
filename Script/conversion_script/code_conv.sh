#!/bin/sh
#sudo apt-get install nkf
find ./src -name '*.txt' -type f -print0 | xargs -0 nkf -u --overwrite -w -Lu
