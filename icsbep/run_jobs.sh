#!/bin/bash

BASEDIR=$PWD

cd $BASEDIR

# Check for argument -- if one exists, we assume it is a file with the list of
# directories to run. Otherwise, we simply search for directories containing a
# settings.xml file
if [[ $# -gt 0 ]]
then
    directories=$(cat $1)
else
    directories=$(find . -name settings.xml | sed 's/\/settings.xml//g' | sort)
fi

for dir in $directories
do
    if [[ $(command -v qsub) ]]
    then
        echo Submitting job for ${dir}...
        cd $BASEDIR/$dir
        qsub openmc.pbs
    else
        echo Running job ${dir}...
        cd $BASEDIR/$dir
        openmc > openmc.stdout 2>&1
    fi
done
