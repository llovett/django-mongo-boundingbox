#!/bin/sh

# mongo.sh
#
# This script is unnecessary on the development server, but if you find yourself
# developing on your laptop, this script can launch the mongodb server for you.
# This assumes you already have mongodb installed, and that the server executable,
# mongod, is somewhere on yout PATH.

if [ `id -u` != 0 ]; then
    echo "Must be root to run this script."
    exit 1
fi

# Set these to your tastes
LOG_DIR="logs"			# Where logs go
LOG_PATH="${LOG_DIR}/mongo.log"	# Name of logfile
DATABASE_PATH="data/db"		# Where to put the database

# Don't touch this
HERE=`pwd`
mkdir -p "${HERE}/${DATABASE_PATH}"
mkdir -p "${HERE}/${LOG_DIR}"
touch "${HERE}/${LOG_PATH}"
chmod 644 "${HERE}/${LOG_PATH}"

mongod --logappend --logpath "${HERE}/${LOG_PATH}" --dbpath "${HERE}/${DATABASE_PATH}" &
