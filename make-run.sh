#!/bin/bash 
# make-run.sh 
# make sure a process is always running.  
# Add the following to the crontab (i.e. crontab -e)
# */5 * * * * /home/path_to_make_run/make-run.sh

process=DiffDetect.py 
makerun="/Users/rakumar/Google\ Drive/git/website_diff_detection/run.sh"  

if ps ax | grep -v grep | grep $process > /dev/null         
then                 
  exit         
else         
  $makerun &
fi 